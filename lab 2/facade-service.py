import uuid
import httpx
import requests
from fastapi import FastAPI

app = FastAPI()

MESSAGES_SERVICE = 'http://127.0.0.1:8001/lab2'
LOGGING_SERVICE = 'http://127.0.0.1:8002/lab2'


@app.post("/lab2", status_code=200)
def message_handler(msg: str):
    httpx.post(LOGGING_SERVICE)
    requests.post(url=LOGGING_SERVICE, json={'uuid': str(uuid.uuid4()), 'msg': msg.msg})


@app.get("/lab2")
def message_handler():
    logging_response = httpx.get(LOGGING_SERVICE).text.strip('"')
    message_response = httpx.get(MESSAGES_SERVICE).text.strip('"')
    return message_response + ': ' + logging_response
