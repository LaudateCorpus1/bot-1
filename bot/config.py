import os
from dotenv import load_dotenv

load_dotenv()

env = os.environ

POSTGRES_USER = env["POSTGRES_USER"]
POSTGRES_PASSWORD = env["POSTGRES_PASSWORD"]
POSTGRES_SERVER = env["POSTGRES_SERVER"]
POSTGRES_PORT = env["POSTGRES_PORT"]
POSTGRES_DB = env["POSTGRES_DB"]

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
