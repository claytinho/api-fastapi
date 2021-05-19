from fastapi import FastAPI
from datetime import date

app = FastAPI()


@app.get("/")
async def root():
    today = str(date.today())
    return {"message": "Hoje é dia: " + today}
