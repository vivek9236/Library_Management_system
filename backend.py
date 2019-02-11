import sqlite3


def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,isbn text,issue text,s_n integer,i_d text,d_d text)")
    conn.commit()
    conn.close()

def insert(title,author,isbn,issue,s_n,i_d,d_d):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?,?,?)",(title,author,isbn,issue,s_n,i_d,d_d))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    print(rows)
    return rows

def search(title="",author="",isbn="",issue="",s_n="",i_d="",d_d=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR isbn=? OR issue=? OR s_n=? OR i_d=? OR d_d=?", (title,author,isbn,issue,s_n,i_d,d_d))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,isbn,issue,s_n,i_d,d_d):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,isbn=?,issue=?,s_n=?,i_d=?,d_d=? WHERE id=?",(title,author,isbn,issue,s_n,i_d,d_d,id))
    conn.commit()
    conn.close()
def count():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT COUNT(*) FROM book")
    number=cur.fetchall()
    conn.commit()
    conn.close()
    return number

connect()
