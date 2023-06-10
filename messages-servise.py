import asyncio
import uvicorn
from fastapi import FastAPI

# Створення FastAPI додатку
app = FastAPI()

# Оголошення обробника для маршруту /message
@app.get("/message")
async def get_message():
    return {'msg': 'not implemented yet'}

# Запуск сервера за допомогою uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)