import sqlite3

class SqliteStorage:

    def __init__(self, dbname):
        self._dbname = dbname

    def persist(self, operation):
        with sqlite3.connect(self._dbname) as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS operations (uid GUID PRIMARY KEY, operand1 REAL, operand2 REAL, calculation TEXT, result REAL, timestamp REAL)")
            c.execute(
                "INSERT INTO operations VALUES ('"
                    + str(operation.uid) + "', "
                    + str(operation.operand1) + ", "
                    + str(operation.operand2) + ", '"
                    + operation.calculation + "', "
                    + str(operation.result) + ", "
                    + str(operation.timestamp) +
                ")"
            )
            conn.commit()

    def retrieve(self, uid):
        with sqlite3.connect(self._dbname) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM operations WHERE uid = '" + str(uid) + "'")
            return c.fetchone()

    def retrieve_all(self):
        with sqlite3.connect(self._dbname) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM operations")
            return c.fetchall()

    def clear(self):
        with sqlite3.connect(self._dbname) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM operations")
            conn.commit()
