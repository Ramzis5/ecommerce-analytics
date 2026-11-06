"""Small database aggregates used by the dashboard's customer page."""

import pandas as pd
from sqlalchemy import column, distinct, extract, func, literal, select, table, union_all


def fetch_event_metrics(engine, selected_years=()):
    """Return funnel counts, raw event counts and distinct sessions.

    Aggregate in PostgreSQL instead of downloading and copying the events table.
    Distinct sessions are counted across the whole selection, not summed across
    years, because the same session can have events in more than one year.
    """
    events = table(
        "events", column("created_at"), column("event_type"), column("session_id")
    )
    selected = select(events.c.event_type, events.c.session_id)
    years = tuple(sorted({int(year) for year in selected_years}))
    if years:
        selected = selected.where(extract("year", events.c.created_at).in_(years))
    filtered = selected.cte("filtered_events")
    normalized_type = func.lower(filtered.c.event_type)

    funnel = (
        select(
            literal("funnel").label("metric"),
            normalized_type.label("event_type"),
            func.count(distinct(filtered.c.session_id)).label("events"),
        )
        .where(filtered.c.event_type.is_not(None))
        .group_by(normalized_type)
    )
    raw_counts = (
        select(
            literal("raw").label("metric"),
            filtered.c.event_type,
            func.count().label("events"),
        )
        .where(filtered.c.event_type.is_not(None))
        .group_by(filtered.c.event_type)
    )
    sessions = select(
        literal("sessions").label("metric"),
        literal(None).label("event_type"),
        func.count(distinct(filtered.c.session_id)).label("events"),
    )
    # One statement keeps the three metrics on the same database snapshot.
    with engine.connect() as connection:
        result = pd.read_sql(union_all(funnel, raw_counts, sessions), connection)

    funnel_counts = result.loc[
        result["metric"] == "funnel", ["event_type", "events"]
    ].reset_index(drop=True)
    event_counts = result.loc[
        result["metric"] == "raw", ["event_type", "events"]
    ].reset_index(drop=True)
    session_count = int(result.loc[result["metric"] == "sessions", "events"].iloc[0])
    return funnel_counts, event_counts, session_count
