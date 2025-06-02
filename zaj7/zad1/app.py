import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# a) Wyświetl tylko sprzedaż produktu „Laptop”
print("a) Sprzedaż produktu 'Laptop':")
cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
for row in cursor.fetchall():
    print(row)

# b) Wyświetl dane tylko z dni 2025-05-07 i 2025-05-08
print("\nb) Sprzedaż z dni 2025-05-07 i 2025-05-08:")
cursor.execute("SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08')")
for row in cursor.fetchall():
    print(row)

# c) Wyświetl tylko transakcje, w których cena jednostkowa przekracza 200 zł
print("\nc) Transakcje z ceną jednostkową > 200 zł:")
cursor.execute("SELECT * FROM sales WHERE price > 200")
for row in cursor.fetchall():
    print(row)

# d) Oblicz łączną wartość sprzedaży dla każdego produktu
print("\nd) Łączna wartość sprzedaży dla każdego produktu:")
cursor.execute("""
    SELECT product, SUM(quantity * price) AS total_sales
    FROM sales
    GROUP BY product
""")
for row in cursor.fetchall():
    print(row)

# e) Znajdź dzień z największą liczbą sprzedanych sztuk
print("\ne) Dzień z największą liczbą sprzedanych sztuk:")
cursor.execute("""
    SELECT date, SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY date
    ORDER BY total_quantity DESC
    LIMIT 1
""")
print(cursor.fetchone())

# Zamknięcie połączenia
conn.close()
