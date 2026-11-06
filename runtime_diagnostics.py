"""Small, payload-free diagnostics for Streamlit Cloud logs."""


def enable_fault_logging():
    """Capture native-fault tracebacks when the host exposes a real stderr."""
    try:
        import faulthandler

        if not faulthandler.is_enabled():
            faulthandler.enable(all_threads=True)
    except (OSError, RuntimeError, ValueError):
        pass


def log_memory(stage):
    """Log peak process RSS on Linux without logging customer data or secrets."""
    try:
        import resource
        import sys

        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        divisor = 1024 * 1024 if sys.platform == "darwin" else 1024
        print(f"[runtime] {stage}: peak_rss_mib={peak / divisor:.1f}", flush=True)
    except (ImportError, OSError, AttributeError):
        pass
