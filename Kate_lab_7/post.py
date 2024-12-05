import psycopg2
from tabulate import tabulate

# Параметри підключення до БД
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="supply_dbt",  # Назва бази даних
    user="admin",                  # Ім'я користувача
    password="root"                # Пароль
)
cur = conn.cursor()

# Функція для виводу структури та даних таблиці
def display_table_structure_and_data(table_name):
    # Структура таблиці
    print(f"\n--- Структура таблиці {table_name} ---")
    cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name.lower()}'")
    structure = cur.fetchall()
    print(tabulate(structure, headers=["Назва колонки", "Тип даних"], tablefmt="psql"))

    # Дані таблиці
    print(f"\n--- Дані таблиці {table_name} ---")
    cur.execute(f"SELECT * FROM {table_name}")
    data = cur.fetchall()
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name.lower()}'")
    headers = [row[0] for row in cur.fetchall()]
    print(tabulate(data, headers=headers, tablefmt="psql"))

# Виведення структури та даних для кожної таблиці
tables = ["suppliers", "materials", "supplies"]
for table in tables:
    display_table_structure_and_data(table)

# Виконання та вивід запитів
queries = {
    "Поставки за 3 або менше днів, відсортовані за алфавітом постачальників": """
        SELECT s.supply_id, s.supply_date, su.company_name, su.contact_person, m.material_name, s.quantity, s.delivery_days
        FROM supplies s
        JOIN suppliers su ON s.supplier_id = su.supplier_id
        JOIN materials m ON s.material_id = m.material_id
        WHERE s.delivery_days <= 3
        ORDER BY su.company_name ASC;
    """,
    "Сума до сплати за кожну поставку": """
        SELECT s.supply_id, su.company_name, m.material_name, s.quantity, m.price, 
               (s.quantity * m.price) AS total_cost
        FROM supplies s
        JOIN suppliers su ON s.supplier_id = su.supplier_id
        JOIN materials m ON s.material_id = m.material_id;
    """,
    "Поставки обраного матеріалу (запит з параметром)": """
        SELECT s.supply_id, s.supply_date, su.company_name, m.material_name, s.quantity
        FROM supplies s
        JOIN suppliers su ON s.supplier_id = su.supplier_id
        JOIN materials m ON s.material_id = m.material_id
        WHERE m.material_name = %s;
    """,
    "Кількість кожного матеріалу, що постачається кожним постачальником": """
        SELECT su.company_name, m.material_name, SUM(s.quantity) AS total_quantity
        FROM supplies s
        JOIN suppliers su ON s.supplier_id = su.supplier_id
        JOIN materials m ON s.material_id = m.material_id
        GROUP BY su.company_name, m.material_name
        ORDER BY su.company_name, m.material_name;
    """,
    "Загальна кількість кожного матеріалу (підсумковий запит)": """
        SELECT m.material_name, SUM(s.quantity) AS total_quantity
        FROM supplies s
        JOIN materials m ON s.material_id = m.material_id
        GROUP BY m.material_name
        ORDER BY m.material_name;
    """,
    "Кількість поставок від кожного постачальника (підсумковий запит)": """
        SELECT su.company_name, COUNT(s.supply_id) AS total_supplies
        FROM supplies s
        JOIN suppliers su ON s.supplier_id = su.supplier_id
        GROUP BY su.company_name
        ORDER BY su.company_name;
    """
}

# Вивід результатів виконання запитів
for description, query in queries.items():
    print(f"\n--- {description} ---")
    try:
        if "з параметром" in description:
            material_name = input("Введіть назву матеріалу для фільтрації: ")
            cur.execute(query, (material_name,))
        else:
            cur.execute(query)
        result = cur.fetchall()
        headers = [desc[0] for desc in cur.description]
        print(tabulate(result, headers=headers, tablefmt="psql"))
    except Exception as e:
        print(f"Помилка виконання запиту: {e}")

cur.close()
conn.close()
