import hazelcast

if __name__ == "__main__":
    # Створюємо клієнта Hazelcast та підключаємось до уже запущеного кластера Hazelcast на 127.0.0.1
    client = hazelcast.HazelcastClient()
    # Отримуємо розподілену мапу з кластера
    distributed_map = client.get_map("my-distributed-map").blocking()
    # Стандартне додавання та отримання значення
    distributed_map.put("key", "value")
    distributed_map.get("key")
    # Методи конкурентної мапи, оптимістичне оновлення
    distributed_map.put_if_absent("somekey", "somevalue")
    distributed_map.replace_if_same("key", "value", "newvalue")
    # Завершуємо роботу з клієнтом Hazelcast
    client.shutdown()