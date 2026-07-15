from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from app.core.config import settings


connection_string = (
    f"mssql+pyodbc://@{settings.DB_SERVER}/"
    f"{settings.DB_DATABASE}"
    f"?driver={quote_plus(settings.DB_DRIVER)}"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
)

engine = create_engine(
    connection_string,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()