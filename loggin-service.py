import asyncio
import uvicorn
import hazelcast
from hazelcast.client import HazelcastClient
from fastapi import FastAPI
from typing import Dict
import requests
from pydantic import BaseModel

# Налаштування клієнта Hazelcast та отримання розподіленої мапи
client = hazelcast.HazelcastClient(
    cluster_members=[
        "127.0.0.1:5701"
    ]
)

distributed_map = client.get_map("distributed-map")

# Оголошення моделі даних
class Log(BaseModel):
    uuid: str
    msg: str

# Створення FastAPI додатку
app = FastAPI()

# Оголошення обробника для створення логу
@app.post("/log")
async def create_log(log: Log):
    await distributed_map.set(log.uuid, log.msg)
    return {'uuid': log.uuid, 'msg': log.msg}

# Оголошення обробника для отримання логу
@app.get("/log")
async def get_log():
    all_values = await distributed_map.values()
    return {'logs': all_values}

# Запуск сервера за допомогою uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)