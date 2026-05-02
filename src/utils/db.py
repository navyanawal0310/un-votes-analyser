from sqlalchemy import create_engine
from sqlalchemy import text

DB_URL = "postgresql://postgres:newpassword123@127.0.0.1:5432/un_votes"

engine = create_engine(DB_URL)
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("DB Connected:", result.scalar())
