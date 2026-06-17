"""Minimal user auth service (demo target for DeployGuard)."""


class AuthService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id: int):
        """Fetch a user by id using a parameterized query."""
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, email, role FROM users WHERE id = %s", (user_id,)
        )
        return cursor.fetchone()

    def get_user_by_email(self, email):
        """Fetch a user by email using a parameterized query."""
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, email, role FROM users WHERE email = %s", (email,)
        )
        return cursor.fetchone()
