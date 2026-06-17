"""Order lookup service (demo target for DeployGuard — planted SQL injection)."""


class OrderService:
    def __init__(self, db):
        self.db = db

    def find_by_customer(self, customer_name):
        cursor = self.db.cursor()
        # VULNERABLE: SQL injection via f-string interpolation of user input
        cursor.execute(
            f"SELECT id, total FROM orders WHERE customer = '{customer_name}'"
        )
        return cursor.fetchall()

    def search_notes(self, term):
        cursor = self.db.cursor()
        # VULNERABLE: SQL injection via string concatenation
        query = "SELECT id FROM orders WHERE note = '" + term + "'"
        cursor.execute(query)
        return cursor.fetchall()
