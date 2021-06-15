from fastapi import FastAPI

app = FastAPI()


@app.get("/lab2")
def post():
    return "In development, expected soon. Thank you for being with us!"
