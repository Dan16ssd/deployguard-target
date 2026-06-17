"""Service health helpers (clean feature — flows through the full DeployGuard chain)."""


def status() -> dict:
    """Return a static health payload for the service."""
    return {"status": "ok", "service": "deployguard-target"}


def uptime_label(seconds: int) -> str:
    """Render an uptime duration as a human-readable 'HhMmSs' label."""
    minutes, sec = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h{minutes}m{sec}s"
