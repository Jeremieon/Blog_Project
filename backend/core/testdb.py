import psycopg2

try:
    conn = psycopg2.connect(
        dbname="blogdb",
        user="postgres",
        password="1990",
        host="localhost",
        port=5432
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
