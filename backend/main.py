from fastapi import FastAPI
from app.db.database import SessionLocal
from sqlalchemy import text

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Zephyn"}

@app.get("/check-db")
def check_db():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1 AS test"))
        return {"status": "success", "result": result.scalar()}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    finally:
        db.close()

