from dotenv import load_dotenv
import os
from sqlalchemy import create_engine,text

load_dotenv("db.env")   # Load .env into environment variables

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

if password is None:
    raise ValueError("DB_PASSWORD is not set in your environment!")

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

'''def load_job_from_db(id):
    with engine.connect() as conn:
        id = int(id)
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
        
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])'''

def load_job_from_db(id):
    id = int(id)
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}
        )
        rows = result.mappings().all()
        if not rows:
            return None
        return dict(rows[0])

#def add_application_to_db(job_id,application):
