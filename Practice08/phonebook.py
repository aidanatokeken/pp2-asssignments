from connect import get_connection

conn = get_connection()
cur = conn.cursor()


# ------------------ FUNCTIONS ------------------

def show_all():
    cur.execute("SELECT * FROM contacts ORDER BY id")
    return cur.fetchall()


def search_contact(text):
    cur.execute("""
        SELECT * FROM contacts
        WHERE name ILIKE %s OR phone ILIKE %s
    """, (f"%{text}%", f"%{text}%"))
    return cur.fetchall()


def add_contact(name, phone):
    cur.execute("""
        INSERT INTO contacts (name, phone)
        VALUES (%s, %s)
    """, (name, phone))
    conn.commit()


def update_contact(name, phone):
    cur.execute("""
        UPDATE contacts
        SET phone = %s
        WHERE name = %s
    """, (phone, name))
    conn.commit()


def delete_contact(value):
    cur.execute("""
        DELETE FROM contacts
        WHERE name = %s OR phone = %s
    """, (value, value))
    conn.commit()


# ------------------ MENU ------------------

def menu():
    while True:
        print("\n📱 PHONEBOOK MENU")
        print("1. Show all contacts")
        print("2. Search contact")
        print("3. Add contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            for row in show_all():
                print(row)

        elif choice == "2":
            text = input("Enter name or phone: ")
            for row in search_contact(text):
                print(row)

        elif choice == "3":
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(name, phone)
            print("Added!")

        elif choice == "4":
            name = input("Name to update: ")
            phone = input("New phone: ")
            update_contact(name, phone)
            print("Updated!")

        elif choice == "5":
            value = input("Name or phone to delete: ")
            delete_contact(value)
            print("Deleted!")

        elif choice == "0":
            print("Bye")
            break

        else:
            print("Invalid option")


# ------------------ RUN ------------------
menu()