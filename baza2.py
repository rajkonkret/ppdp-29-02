# baza sql - relacyjna baza danych
import sqlite3

try:
    conn = sqlite3.connect("baza_sqlite.db")  # połączenie z bazą danych
    # conn = sqlite3.connect(":memory:")  # połączenie z bazą danych w pamieci
    c = conn.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''
    print("Baza danych została podłaczona")

    with open("tables.sql", "r") as f:
        sql_script = f.read()

    # c.execute(query)
    # conn.commit()
    c.executescript(sql_script)
    conn.commit()

except sqlite3.Error as e:
    print("Błąd połączenia z bazą danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie z bazą danych zostało zamknięte")
# exit(1)
