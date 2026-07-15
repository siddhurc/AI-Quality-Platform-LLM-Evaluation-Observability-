from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    DB_SERVER = os.getenv("DB_SERVER")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_DRIVER = os.getenv("DB_DRIVER")


settings = Settings()