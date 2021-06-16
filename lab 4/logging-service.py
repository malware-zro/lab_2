from models import Message
from fastapi import FastAPI
import hazelcast


app = FastAPI()
hash_hazelcast = hazelcast.HazelcastClient().get_map('my_map')


@app.post('/lab4', status_code=200)
def post(message: Message):
    hash_hazelcast.put(message.uuid, message.msg)
    print(message)


@app.get('/lab4')
def get():
    return hash_hazelcast.entry_set().result()

