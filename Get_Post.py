import requests
import uuid

msg_uuid = uuid.uuid4() # Генерується унікальний ідентифікатор UUID за допомогою функції uuid4() з модуля uuid


get_response = requests.get('http://localhost:5000') # Виконується GET-запит до адреси 'http://localhost:5000' за допомогою функції get() з модуля requests. Отриману відповідь зберігається в змінну get_response
print("GET Response:") #  Виводиться повідомлення "GET Response:"
print(get_response.text) # Виводиться вміст отриманої відповіді в форматі тексту


post_response = requests.post('http://localhost:5000', json={"uuid": str(msg_uuid), "msg": "Hello, world!"}) # Виконується POST-запит до адреси 'http://localhost:5000' за допомогою функції post() з модуля requests. У тілі запиту передається JSON-об'єкт з полями "uuid" і "msg". Отриману відповідь зберігається в змінну post_response
print("POST Response:") # Виводиться повідомлення "POST Response:
print(post_response.text) # Виводиться вміст отриманої відповіді на POST-запит в форматі тексту

# Запит GET до logging-service
get_response = requests.get('http://localhost:5001')
print("GET Response from logging service:")
print(get_response.text)

# Запит GET до message-service
get_response = requests.get('http://localhost:5002')
print("GET Response from message service:")
print(get_response.text)