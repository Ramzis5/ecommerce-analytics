# Streamlit stability patch

Prepared against GitHub revision `3daa415` (`Ramzis5/ecommerce-analytics`).

## Diagnosis

The generic Streamlit error screenshot does not establish a root cause. The
public homepage loaded during inspection. The user later supplied the Cloud
log exported on November 6, 2026. It records successful dependency installation
and server startup, then deprecated-width warnings; it contains no traceback,
OOM/Killed message, actual segmentation fault, or database exception.

Cloud detected PyArrow 26.0.1 and successfully replaced it with 24.0.0 before
the server started. This is a preventive compatibility correction, not evidence
that this particular server crashed from Arrow. The upstream native-thread
fault is documented at https://github.com/apache/arrow/issues/50471.
No Supabase credentials or authenticated production dashboard session were
available for verification.

The strongest code-supported hypothesis is application memory pressure:

- The original loader fetched every raw event with nine columns, stored the
  data in the shared serialized cache and each user's session, then copied
  events on every rerun into an unused variable.
- Opening Customer & Conversion copied the full events table again.
- Opening Export & Reports immediately built both a full sales CSV and an
  object-heavy Excel workbook.
- Opening Churn Prediction trained three models plus five Random Forest
  cross-validation fits; each Random Forest used all available workers.

A separate confirmed bug made both churn cache keys ignore every input,
including the intended hash argument, because all parameter names began with
an underscore. Data refreshes could therefore reuse models from an older
snapshot.

## Changes

- Aggregate event counts and distinct sessions in SQL, on demand, with a
  bounded small-result cache. Preserve the original year-only event filtering
  and deduplicate sessions across the entire selected period.
- Remove unused event copies and narrow trend intermediates to two columns.
- Generate large sales files after an explicit preparation click. Stream
  Excel rows; export timezone-aware dates as timezone-free UTC values.
- Fingerprint all relevant churn input values; bound and expire ML caches;
  use one worker; guard small classes and insufficient forecasting history.
- Log page/data-load boundaries with process peak RSS, without customer data
  or credentials. Peak RSS is not current RSS and does not by itself prove OOM.
- Enable Python's native-fault traceback handler where supported. This can
  expose a SIGSEGV traceback, but cannot catch an OS OOM kill.
- Keep an explicit `pyarrow<25` compatibility cap matching Cloud's mitigation.
- Replace deprecated `use_container_width` arguments with supported `width`
  values so those warnings no longer obscure later diagnostic messages.
- Correct README entrypoint and secrets section names.

## Apply

1. Copy all files from the ZIP into the repository, keeping the directory
   structure. The required runtime changes are `DataVita.py`, `data_runtime.py`,
   `ml_reliability.py`, `export_runtime.py`, `runtime_diagnostics.py`, and
   `requirements.txt`. Tests and documentation are included.
2. Commit those changes to the branch used by Streamlit Community Cloud.
   Keep the app entrypoint as `DataVita.py`; keep existing working `[postgres]`
   secrets. No database schema change is required.
3. After redeployment, check Customer & Conversion with one and multiple
   selected years, the forecast horizon, churn, and prepared CSV/Excel downloads.
4. If it fails again, retain the Cloud log lines immediately before/after the
   failure, including `[runtime]` markers and any OOM/Killed, health-check,
   database timeout or Python traceback messages. Redact secrets.

The patch is prepared locally; it has not been pushed or deployed.

## Validation and limits

27 offline tests passed against both the initial development stack and the
main package versions shown in the supplied Cloud log. After the follow-up
changes (width migration and fault diagnostics), all 27 tests were rerun
against the Cloud-matching package stack and passed. Python compilation and
`git diff --check` also passed.
Tests cover event equivalence (nulls, mixed case, repeated sessions and multiple
years), PostgreSQL SQL compilation, cache invalidation, small-class handling,
forecast bounds, Excel contents and deferred generation. Streamlit AppTest
renders eight page bodies and exercises repeated reruns and a real filter
change; its harness dispatches callable pages directly rather than testing
browser navigation links. Inputs are synthetic and no production database is
queried. ML cache tests use lightweight estimators to check cache behavior,
not the training performance of the full production dataset.

Initial validation runtime: Python 3.12, Streamlit 1.51.0, pandas 2.2.3,
scikit-learn 1.8.0, SQLAlchemy 2.1.8, Plotly 6.9.0.

Follow-up validation runtime: Python 3.12, Streamlit 1.67.0, pandas 3.1.1,
NumPy 2.5.4, Plotly 7.1.0, SQLAlchemy 2.1.8, psycopg2-binary 2.9.13,
scikit-learn 1.9.1, imbalanced-learn 0.14.2, openpyxl 3.1.5 and PyArrow 24.0.0.
This matches the logged primary package versions, not the remote host's
hardware, Python patch version, database or workload.

The new event query still scans/aggregates data in Supabase on a cache miss.
Its actual latency, database limits, and real deployment memory usage remain
to be measured. Sales and user frames still occupy per-session memory, and
the first ML fit still takes time. These changes reduce identified pressure;
they are not proof that a free plan can handle unlimited data or concurrency.

Existing hard-coded churn presentation metrics, SMOTE status/counts, and
customer totals were left unchanged. They are not fresh model evaluation
results and warrant a separate analytical correctness review.
