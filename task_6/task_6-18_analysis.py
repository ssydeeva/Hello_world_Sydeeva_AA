"""
Анализ данных из PostgreSQL (база taskdb)
"""

import pandas as pd
import numpy as np
import psycopg

# ──────────────────────────────────────────────────────────────
# 1. Подключение к PostgreSQL
# ──────────────────────────────────────────────────────────────

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="taskdb",
    user="student",
    password="student"
)
print("✅ Подключение к PostgreSQL установлено корректно")
print(f"   База данных: taskdb")
print(f"   Пользователь: student")
print(f"   Хост: localhost:5432\n")

# ──────────────────────────────────────────────────────────────
# 2. SQL-запрос с JOIN и загрузка в DataFrame
# ──────────────────────────────────────────────────────────────

query = """
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.category,
    pr.id AS price_id,
    pr.price,
    pr.created_at
FROM products AS p
JOIN prices AS pr ON p.id = pr.product_id
ORDER BY p.id, pr.price
"""

df = pd.read_sql_query(query, conn)

print("=" * 70)
print("2. Данные загружены в DataFrame")
print(f"   Количество записей: {len(df)}")
print(f"   Столбцы: {list(df.columns)}")
print(f"\nПервые 10 строк:")
print(df.head(10).to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────
# 3. Статистические показатели по цене
# ──────────────────────────────────────────────────────────────

print("=" * 70)
print("3. Статистические показатели по столбцу price (руб.)")
print("-" * 70)

mean_price = df['price'].mean()
median_price = df['price'].median()
std_price = df['price'].std()
min_price = df['price'].min()
max_price = df['price'].max()

print(f"   Среднее значение (mean):        {mean_price:>12.2f} руб.")
print(f"   Медиана (median):               {median_price:>12.2f} руб.")
print(f"   Стандартное отклонение (std):   {std_price:>12.2f} руб.")
print(f"   Минимальная цена (min):         {min_price:>12.2f} руб.")
print(f"   Максимальная цена (max):        {max_price:>12.2f} руб.")
print()

# ──────────────────────────────────────────────────────────────
# 4. Квартили, межквартильный размах и товары-выбросы
# ──────────────────────────────────────────────────────────────

print("=" * 70)
print("4. Квартильный анализ и товары с ценой выше Q3")
print("-" * 70)

Q1 = df['price'].quantile(0.25)
Q2 = df['price'].quantile(0.50)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

print(f"   Первый квартиль (Q1):           {Q1:>12.2f} руб.")
print(f"   Второй квартиль (Q2/медиана):   {Q2:>12.2f} руб.")
print(f"   Третий квартиль (Q3):           {Q3:>12.2f} руб.")
print(f"   Межквартильный размах (IQR):    {IQR:>12.2f} руб.")
print()

outliers = df[df['price'] > Q3][['product_name', 'category', 'price']]
outliers = outliers.sort_values('price', ascending=False)
outliers_unique = outliers.drop_duplicates(subset=['product_name', 'category'])

print(f"   Количество записей с ценой выше Q3: {len(outliers)}")
print(f"   Из них уникальных товаров: {len(outliers_unique)}")
print(f"\n   Товары с ценой выше Q3:")
print(outliers_unique.head(20).to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────
# 5. Группировка по категориям
# ──────────────────────────────────────────────────────────────

print("=" * 70)
print("5. Статистики по категориям товаров")
print("-" * 70)

category_stats = df.groupby('category').agg(
    record_count=('price', 'count'),
    mean_price=('price', 'mean'),
    median_price=('price', 'median'),
    std_price=('price', 'std')
).round(2)

category_stats = category_stats.sort_values('mean_price', ascending=False)

print(category_stats.to_string())
print()

# ──────────────────────────────────────────────────────────────
# 6. Топ-5 товаров с наибольшим разбросом цен
# ──────────────────────────────────────────────────────────────

print("=" * 70)
print("6. Топ-5 товаров с наибольшим разбросом цен")
print("-" * 70)

price_range = df.groupby(['product_name', 'category']).agg(
    min_price=('price', 'min'),
    max_price=('price', 'max')
).round(2)

price_range['price_diff'] = price_range['max_price'] - price_range['min_price']
price_range = price_range.sort_values('price_diff', ascending=False)

print(price_range.head(5).to_string())
print()

conn.close()
print("✅ Анализ завершён. Соединение закрыто.")