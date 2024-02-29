# baza sql - relacyjna baza danych
import sqlite3

try:
    conn = sqlite3.connect("baza_sqlite.db")  # połączenie z bazą danych
    c = conn.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Błąd połączenia z bazą danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie z bazą danych zostało zamknięte")
