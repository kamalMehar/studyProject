from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS homework_files CASCADE")
    cursor.execute("DROP TABLE IF EXISTS homework_submissions CASCADE")
    cursor.execute("DROP TABLE IF EXISTS homeworks CASCADE")
    print("Dropped homework tables to start fresh with UUID columns")

