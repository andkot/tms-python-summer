import psycopg2

# connecting to the DB
conn = psycopg2.connect("dbname='test_db' user='test_user' host='localhost' password='091294'")

# cursor
cur = conn.cursor()

# execute query
cur.execute("select id, first_name from person")

rows = cur.fetchall()

for r in rows:
    print(f'id: {r[0]}; first_name: {r[1]}')

# close the cursor
cur.close()

# close the connection
conn.close()
