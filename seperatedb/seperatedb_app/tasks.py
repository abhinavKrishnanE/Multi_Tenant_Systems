import psycopg2

from django.conf import settings
from django.db import connections
from django.core.management import call_command
from django.db import connections, DEFAULT_DB_ALIAS

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tenant_database(db_name):

    default_db = settings.DATABASES[DEFAULT_DB_ALIAS]
    conn = psycopg2.connect(
        dbname=default_db["NAME"],
        user=default_db["USER"],
        password=default_db.get("PASSWORD", ""),
        host=default_db["HOST"],
        port=default_db["PORT"],
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f'CREATE DATABASE "{db_name}"')

    cursor.close()
    conn.close()


def add_tenant_database(db_name):
    alias = str(db_name)

    default_db = settings.DATABASES["default"]

    config = {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": db_name,
        "USER": default_db.get("USER", "postgres"),
        "PASSWORD": default_db.get("PASSWORD", ""),
        "HOST": default_db.get("HOST", "localhost"),
        "PORT": default_db.get("PORT", "5432"),

        "ATOMIC_REQUESTS": default_db.get("ATOMIC_REQUESTS", False),
        "AUTOCOMMIT": default_db.get("AUTOCOMMIT", True),
        "CONN_MAX_AGE": default_db.get("CONN_MAX_AGE", 0),
        "CONN_HEALTH_CHECKS": default_db.get("CONN_HEALTH_CHECKS", False),
        "OPTIONS": default_db.get("OPTIONS", {}),

        "TIME_ZONE": getattr(settings, "TIME_ZONE", "UTC"),
    }

    settings.DATABASES[alias] = config
    connections.databases[alias] = config
    return alias


def run_migrations(alias):
    call_command("migrate", database=alias, interactive=False)