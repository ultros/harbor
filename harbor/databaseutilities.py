import sqlite3


class DatabaseUtilities:

    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

    def connect_database(self):
        self.connection = sqlite3.connect(self.database_path)

    def insert_record(self, ip: str, port: int):
        """Insert a record into the database."""
        parameters = (ip, port)

        sql = '''INSERT INTO hosts (ip, port) VALUES (?, ?);'''

        self.cursor.execute(sql, parameters)
        self.connection.commit()

    def create_table(self):
        self.connection.execute("""
        CREATE TABLE "hosts" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "ip" TEXT,
        "port" INTEGER);
        """)
        self.connection.commit()

    def select_all(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT * FROM "hosts"
        """)
        result = cursor.fetchall()
        cursor.close()

        return result

    def select_record(self):
        self.cursor.execute("""
        SELECT * FROM "hosts"
        WHERE""")


class DatabaseManagement(DatabaseUtilities):

    def __init__(self):
        pass

    def dedupe_database(self):
        pass
