# baza sql - relacyjna baza danych
import sqlite3

try:
    conn = sqlite3.connect("baza_sqlite.db")  # połączenie z bazą danych
    c = conn.cursor()
    print("Baza danych została podłaczona")

    insert = """
    INSERT INTO software (id,name,price) VALUES (1, 'Python',200);
    """

    insert_from_data = """
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    """

    select_all = """
    SELECT * FROM software;
    """

    update = """
    UPDATE software SET price =1000 WHERE id =2;
    """

    delete = """
    DELETE FROM software WHERE id =1;
    """
    for row in c.execute(select_all):
        print(row)  # (1, 'Python', 200.0)

    c.execute(select_all)
    for row in c.fetchall():
        print(row)  # (1, 'Python', 200.0)

    # c.execute(insert)
    # conn.commit()

    # c.execute(insert_from_data, (2, 'Java', 100))
    # conn.commit()

    # c.execute(update)
    # conn.commit()

    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Błąd połączenia z bazą danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie z bazą danych zostało zamknięte")
