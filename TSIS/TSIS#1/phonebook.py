from connect import get_connection

conn = get_connection()
cur = conn.cursor()


# ---------------- SHOW ALL ----------------
def show_all():
    cur.execute("SELECT * FROM contacts ORDER BY id")
    return cur.fetchall()


# ---------------- ADD CONTACT ----------------
def add_contact():
    try:
        name = input("Name: ")
        email = input("Email: ")
        birthday = input("Birthday (YYYY-MM-DD): ")

        # simple validation
        if len(birthday) != 10:
            print("Wrong date format! Use YYYY-MM-DD")
            return

        cur.execute("""
            INSERT INTO contacts (name, email, birthday)
            VALUES (%s, %s, %s)
        """, (name, email, birthday))

        conn.commit()
        print("Contact added!")

    except Exception as e:
        print("Error:", e)


# ---------------- SEARCH ----------------
def search():
    text = input("Search text: ")

    cur.execute("""
        SELECT * FROM contacts
        WHERE name ILIKE %s OR email ILIKE %s
    """, (f"%{text}%", f"%{text}%"))

    print(cur.fetchall())


# ---------------- DELETE ----------------
def delete():
    value = input("Name or phone: ")

    cur.execute("""
        DELETE FROM contacts
        WHERE name = %s OR email = %s
    """, (value, value))

    conn.commit()
    print("Deleted")


# ---------------- ADD PHONE ----------------
def add_phone():
    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    cur.execute("""
        SELECT id FROM contacts WHERE name=%s
    """, (name,))

    result = cur.fetchone()

    if result:
        cur.execute("""
            INSERT INTO phones (contact_id, phone, type)
            VALUES (%s, %s, %s)
        """, (result[0], phone, ptype))

        conn.commit()
        print("Phone added")
    else:
        print("Contact not found")


# ---------------- MENU ----------------
def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Show all")
        print("2. Add contact")
        print("3. Search")
        print("4. Delete")
        print("5. Add phone")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            for row in show_all():
                print(row)

        elif choice == "2":
            add_contact()

        elif choice == "3":
            search()

        elif choice == "4":
            delete()

        elif choice == "5":
            add_phone()

        elif choice == "0":
            print("Bye")
            break

        else:
            print("Invalid option")


menu()