from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM django_migrations WHERE app='homework'")
    print("Successfully deleted homework migrations from django_migrations")

