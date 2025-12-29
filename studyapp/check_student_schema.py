from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students' AND column_name = 'id'")
    col = cursor.fetchone()
    print(f"Table students id column: {col}")

