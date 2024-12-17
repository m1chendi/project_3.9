CREATE TABLE IF NOT EXISTS gardener (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id)
);
