from django.db import connection
from django.core.management import call_command

def create_tenant_schema(schema_name):

    with connection.cursor() as cursor:
        cursor.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"')
        cursor.execute(f'SET search_path TO "{schema_name}"')

    call_command("migrate", run_syncdb=True, verbosity=0)

    with connection.cursor() as cursor:
        public = "public"
        cursor.execute(f"SET search_path TO {public}")