from dotenv import load_dotenv
import os
from sqlalchemy import create_engine,text

load_dotenv()  # Load .env into environment variables

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

# URL-encode special characters in password (like @)
from urllib.parse import quote_plus
password = quote_plus(password)

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4"
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        rows = result.mappings().all()  # RowMapping objects

        # Convert RowMapping → dict
        jobs = [dict(row) for row in rows]
        return jobs
