'''
to fetch data from my tables in
postgres database
'''
import psycopg2

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",        # or your server IP
        database="postgres",
        user="postgres",
        password="root",
        port="5432"              # default PostgreSQL port
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT name FROM msultan.employees;")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the data
    for row in rows:
        print(row)
    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)