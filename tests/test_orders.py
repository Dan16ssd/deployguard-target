from app.orders import OrderService


class _Cursor:
    def execute(self, q, params=None):
        self.q = q

    def fetchall(self):
        return [(1, 100)]


class _DB:
    def cursor(self):
        return _Cursor()


def test_find_by_customer():
    assert OrderService(_DB()).find_by_customer("acme") == [(1, 100)]
