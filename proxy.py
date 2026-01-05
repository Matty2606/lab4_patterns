from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql):
        pass

class RealDatabase(Database):
    def query(self, sql):
        print(f"Executing query: {sql}")

class DatabaseProxy(Database):
    def __init__(self, has_access):
        self.real_db = RealDatabase()
        self.has_access = has_access

    def query(self, sql):
        if self.has_access:
            self.real_db.query(sql)
        else:
            print("Access denied. Query cannot be executed.")

if __name__ == "__main__":
    user_db = DatabaseProxy(False)
    admin_db = DatabaseProxy(True)
    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")
