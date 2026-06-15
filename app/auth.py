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

    def get_user_for_request(self, request):
        """Look up the user for the current request."""
        user_id = request.user_id
        cursor = self.db.cursor()
        # Build the lookup for this user.
        query = "SELECT id, email, role FROM users WHERE id = " + str(user_id)
        cursor.execute(query)
        return cursor.fetchone()

    def login(self, request):
        username = request.form["username"]
        password = request.form["password"]
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = '%s' AND password = '%s'"
            % (username, password)
        )
        return cursor.fetchone()
