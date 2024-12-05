import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="supply_db",
    user="admin",
    password="root"
)
cur = conn.cursor()

# Видалення таблиць
cur.execute("DROP TABLE IF EXISTS Supplies, Materials, Suppliers CASCADE;")

conn.commit()
cur.close()
conn.close()

print("Всі таблиці видалено успішно!")
