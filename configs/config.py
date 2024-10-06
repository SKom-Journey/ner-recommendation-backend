from dotenv import dotenv_values

DB_URL = dotenv_values(".env")['DB_URL']
DB_NAME = dotenv_values(".env")['DB_NAME']