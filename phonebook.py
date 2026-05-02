import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5433"
)

cur = conn.cursor()

print("Connected successfully!")