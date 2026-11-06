"""Small, deterministic guards for the dashboard's on-demand ML pages."""

from hashlib import blake2b
import json

import pandas as pd


def fingerprint_frames(*frames: pd.DataFrame) -> str:
    """Hash every row, its order, and the schema instead of a lossy row/sum key."""
    digest = blake2b(digest_size=20)
    for frame in frames:
        schema = {
            "shape": frame.shape,
            "columns": [str(column) for column in frame.columns],
            "dtypes": [str(dtype) for dtype in frame.dtypes],
        }
        digest.update(json.dumps(schema, sort_keys=True).encode("utf-8"))
        row_hashes = pd.util.hash_pandas_object(frame, index=True, categorize=True)
        digest.update(row_hashes.to_numpy().tobytes())
    return digest.hexdigest()


def churn_training_error(
    target: pd.Series, *, min_rows: int = 50, cv_splits: int = 5
) -> str | None:
    """Check both the stratified holdout and the requested cross-validation."""
    counts = target.value_counts()
    if len(target) < min_rows or len(counts) != 2:
        return "Nicht genügend Daten oder keine Varianz in der Churn-Variable."
    if int(counts.min()) < cv_splits:
        return (
            f"Für das Churn-Training werden mindestens {cv_splits} Kunden "
            "pro Klasse (Aktiv und Churned) benötigt."
        )
    return None


def forecast_max_horizon(
    n_months: int, *, minimum_training_months: int = 6, limit: int = 12
) -> int:
    """Leave training data when a user narrows the forecast's date range."""
    return max(0, min(limit, n_months - minimum_training_months))
