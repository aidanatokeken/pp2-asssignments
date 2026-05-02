from connect import get_connection
import csv

conn = get_connection()
cur = conn.cursor()

# CREATE TABLE
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name TEXT,
            phone TEXT
        );
    """)
    conn.commit()

# INSERT ONE CONTACT
def insert_contact(name, phone):
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()

# INSERT FROM CSV
def insert_from_csv(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                row
            )
    conn.commit()

# UPDATE CONTACT
def update_phone(name, new_phone):
    cur.execute(
        "UPDATE contacts SET phone = %s WHERE name = %s",
        (new_phone, name)
    )
    conn.commit()

# SELECT (FILTERS)
def search_by_name(name):
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name}%",))
    return cur.fetchall()

def search_by_prefix(prefix):
    cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
    return cur.fetchall()

# DELETE
def delete_contact(name_or_phone):
    cur.execute(
        "DELETE FROM contacts WHERE name = %s OR phone = %s",
        (name_or_phone, name_or_phone)
    )
    conn.commit()

# SHOW ALL
def show_all():
    cur.execute("SELECT * FROM contacts")
    return cur.fetchall()


# ----------------- TEST -----------------
create_table()

insert_contact("Aida", "87001234567")

print("ALL:", show_all())
print("SEARCH:", search_by_name("Aid"))
print(show_all())