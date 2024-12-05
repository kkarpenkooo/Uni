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

# Створення таблиць
cur.execute("""
    CREATE TABLE IF NOT EXISTS Suppliers (
        supplier_id SERIAL PRIMARY KEY,
        company_name VARCHAR(100) NOT NULL,
        contact_person VARCHAR(50),
        phone VARCHAR(15) CHECK (phone ~ '^[0-9]{10}$'),
        bank_account VARCHAR(20)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Materials (
        material_id SERIAL PRIMARY KEY,
        material_name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL CHECK (price > 0)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Supplies (
        supply_id SERIAL PRIMARY KEY,
        supply_date DATE NOT NULL,
        supplier_id INT REFERENCES Suppliers(supplier_id),
        material_id INT REFERENCES Materials(material_id),
        delivery_days INT CHECK (delivery_days BETWEEN 1 AND 7),
        quantity INT NOT NULL CHECK (quantity > 0)
    );
""")

# Закриваємо підключення
conn.commit()
cur.close()
conn.close()

print("Таблиці створено успішно!")
