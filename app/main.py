from fastapi import FastAPI

from routers import user
from routers import company
from routers import task
from routers import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(company.router)
app.include_router(task.router)


@app.get("/")
def health_check():
    return "OK"
