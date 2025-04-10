from sqlalchemy import create_engine,text

engine = create_engine(
    "mysql+pymysql://root:Noddy%400771@127.0.0.1/NextGen_Careers?charset=utf8mb4"
 )

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        rows = result.mappings().all()  # RowMapping objects

        # Convert RowMapping → dict
        jobs = [dict(row) for row in rows]
        return jobs
