import sqlite3
conn=sqlite3.connect("none.db")
cursor=conn.cursor()
cursor.execute("create table if not exists users (id integer primary key autoincrement,username text not null unique, password text not null)")
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("dbmsexam1", "the password is 8 stars"))
    conn.commit()
    print("User added successfully.")
except sqlite3.IntegrityError:
    print("Username already exists.")
conn.commit()
conn.close() 