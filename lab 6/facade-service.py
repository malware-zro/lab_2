import random
import uuid
import requests
from models import FacadePostMessage
from fastapi import FastAPI
import pika


MESSAGES_SERVICE = ('http://127.0.0.1:8001/lab6',
                    'http://127.0.0.1:8002/lab6')

LOGGING_SERVICE = ('http://127.0.0.1:8011/lab6',
                   'http://127.0.0.1:8012/lab6',
                   'http://127.0.0.1:8013/lab6')


def get_log_host():
    return random.choice(LOGGING_SERVICE)


def get_msg_host():
    return random.choice(MESSAGES_SERVICE)


def put_msg_mq(msg):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='lab6')
    channel.basic_publish(exchange='', routing_key='lab6', body=msg)
    connection.close()


app = FastAPI()


@app.get('/facade_service/')
def get():
    logging_response = requests.get(get_log_host()).text.strip('"')
    message_response = requests.get(get_msg_host()).text.strip('"')
    return logging_response + ': ' + message_response


@app.post("/facade_service/", status_code=200)
def post(msg: FacadePostMessage):
    requests.post(url=get_log_host(), json={'uuid': str(uuid.uuid4()), 'msg': msg.msg})
    put_msg_mq(msg.msg)