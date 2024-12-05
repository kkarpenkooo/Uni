import psycopg2

# Підключення до БД
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="supply_db",
    user="admin",
    password="root"
)
cur = conn.cursor()
import psycopg2

# Заповнення таблиці постачальників
suppliers = [
    ('ТОВ "Постачальник1"', 'Іван Іванов', '0501234567', 'UA1234567890'),
    ('ТОВ "Постачальник2"', 'Марія Петрівна', '0502345678', 'UA9876543210'),
    ('ТОВ "Постачальник3"', 'Олексій Сидоров', '0503456789', 'UA4567891234')
]

for supplier in suppliers:
    cur.execute("""
        INSERT INTO Suppliers (company_name, contact_person, phone, bank_account)
        VALUES (%s, %s, %s, %s);
    """, supplier)

# Заповнення таблиці матеріалів
materials = [
    ('Дерево', 500),
    ('Метал', 1000),
    ('Скло', 700)
]
for material in materials:
    cur.execute("""
        INSERT INTO Materials (material_name, price)
        VALUES (%s, %s);
    """, material)

# Заповнення таблиці поставок
supplies = [
    ('2024-11-01', 1, 1, 5, 50),
    ('2024-11-03', 2, 2, 3, 100),
    ('2024-11-05', 3, 3, 7, 30)
]
for supply in supplies:
    cur.execute("""
        INSERT INTO Supplies (supply_date, supplier_id, material_id, delivery_days, quantity)
        VALUES (%s, %s, %s, %s, %s);
    """, supply)

conn.commit()
cur.close()
conn.close()

print("Дані додано успішно!")
