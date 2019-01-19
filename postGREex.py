import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='ironhair394' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='ironhair394' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='ironhair394' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='ironhair394' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    conn.commit()
    rows= cur.fetchall()
    print(rows)
    conn.close()

def update(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='ironhair394' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store  set item = 'Orange Juice' WHERE item=%s", (item,))
    conn.commit()
    conn.close()
    

create_table()
insert('Wine bottles', 500, 200)
update('Wine bottles')
delete('Orange Juice')
view()
