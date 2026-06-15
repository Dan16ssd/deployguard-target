from app.auth import AuthService


class _Cursor:
    def execute(self, q, params=None):
        self.last = (q, params)

    def fetchone(self):
        return (1, "a@b.com", "user")


class _DB:
    def cursor(self):
        return _Cursor()


def test_get_user_parameterized():
    assert AuthService(_DB()).get_user(1) == (1, "a@b.com", "user")
