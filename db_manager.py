from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlRelationalTableModel, QSqlRelation

def initialize_database():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("tree_clicker.db")

    if not db.open():
        raise Exception("Не удалось подключиться к базе данных.")

    query = QSqlQuery()
    query.exec(
        """
        CREATE TABLE IF NOT EXISTS gardener (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            salary INTEGER NOT NULL,
            department_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES department(id)
        )
        """
    )

    query.exec(
        """
        CREATE TABLE IF NOT EXISTS department (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
    )

   
    query.exec("INSERT OR IGNORE INTO department (name) VALUES ('Садоводство'), ('Ландшафтный дизайн'), ('Огородничество')")

    return db

def create_department_model(db):
    model = QSqlRelationalTableModel()
    model.setTable("department")
    model.select()
    return model

