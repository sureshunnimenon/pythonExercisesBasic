import sqlite3

# connect to database
conn = sqlite3.connect("data1.db")

# create cursor object
cur = conn.cursor()

# write an sql query
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES ('Wine glass', 10, 23.50)")
cur.execute("SELECT * FROM store")
rows= cur.fetchall()

# print rows as python list, which is similar to arrays in javascript
print(rows)   

# commit changes to database
conn.commit()

# close connection
conn.close()

# function to delete data
def delete(item):
    conn = sqlite3.connect("data1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()

    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()

    print(rows)

    conn.close()
    return 1

def insert(item, quantity, price):
    conn = sqlite3.connect("data1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()

    print(rows)

    conn.close()
    return 1
       

delete('Wine glass')
insert('ExBracelet', 200, 10)


