from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name LIKE 'homework%'")
    tables = cursor.fetchall()
    print(f"Existing homework tables: {tables}")
    
    if tables:
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}' AND column_name = 'id'")
            col = cursor.fetchone()
            print(f"Table {table_name} id column: {col}")

