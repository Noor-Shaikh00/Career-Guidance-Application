import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            qualification TEXT,
            interest TEXT,
            phone TEXT,
            career TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_student(name, age, qualification, interest, phone, career_list):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # ✅ Convert list to string
    career_str = "\n".join(career_list)

    cur.execute("""
    INSERT INTO students (name, age, qualification, interest, phone, career)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, age, qualification, interest, phone, career_str))

    conn.commit()
    conn.close()



# import sqlite3


# def save_student(name, age, qualification, interest, phone, career_list):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()

#     # ✅ Convert list to string
#     career_str = "\n".join(career_list)

#     cur.execute("""
#     INSERT INTO students (name, age, qualification, interest, phone, career)
#     VALUES (?, ?, ?, ?, ?, ?)
#     """, (name, age, qualification, interest, phone, career_str))

#     conn.commit()
#     conn.close()



# import sqlite3

# def create_db():
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         age INTEGER,
#         qualification TEXT,
#         interest TEXT,
#         phone TEXT,
#         career TEXT
#     )
#     """)

#     conn.commit()
#     conn.close()

# def save_student(name, age, qualification, interest, phone, career):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()

#     cur.execute("""
#     INSERT INTO students (name, age, qualification, interest, phone, career)
#     VALUES (?, ?, ?, ?, ?, ?)
#     """, (name, age, qualification, interest, phone, career))

#     conn.commit()
#     conn.close()
