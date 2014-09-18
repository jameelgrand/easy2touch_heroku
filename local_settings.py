
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "73a20302-1317-4a6c-9697-5bea4dbe91368be8e53b-ee8c-4f95-beca-0a1a03c3b091282425d1-f0eb-4a47-a186-30c0408c9cd2"
NEVERCACHE_KEY = "77d5f8d1-eb5b-4e4c-bed7-4fb66d845b6ad65ce4bb-3321-4505-a557-6c586d08fc8931c42895-e507-4ddd-aee3-c65cd82a363e"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
