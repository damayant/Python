from fastapi import FastAPI
from database import engine, Base
import health,authors

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API with FastAPI & PostgreSQL")


app.include_router(health.router)
app.include_router(authors.router)
