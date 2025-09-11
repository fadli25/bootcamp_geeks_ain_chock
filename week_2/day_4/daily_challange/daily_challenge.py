import psycopg2
import requests
import random

connection = psycopg2.connect(
    dbname="countries_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
connection.autocommit = True

with connection.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            capital VARCHAR(100),
            flag TEXT,
            subregion VARCHAR(100),
            population BIGINT
        )
    """)

url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"
response = requests.get(url)
data = response.json()

random_countries = random.sample(data, 10)

with connection.cursor() as cur:
    for country in random_countries:
        name = country.get("name", {}).get("common", "N/A")
        capital = country.get("capital", ["N/A"])[0] if country.get("capital") else "N/A"
        flag = country.get("flags", {}).get("png", "N/A")
        subregion = country.get("subregion", "N/A")
        population = country.get("population", 0)

        cur.execute("""
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, capital, flag, subregion, population))

print("✅ 10 random countries inserted successfully!")
