from app.health import status, uptime_label


def test_status_ok():
    assert status()["status"] == "ok"


def test_uptime_label():
    assert uptime_label(3661) == "1h1m1s"
