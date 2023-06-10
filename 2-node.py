import hazelcast

if __name__ == "__main__":
    # Починаємо клієнта Hazelcast і підключаємося до уже запущеного кластера Hazelcast на 127.0.0.1
    client = hazelcast.HazelcastClient()
    # Отримуємо розподілену мапу з кластера.
    distributed_map = client.get_map("my-distributed-map").blocking()
    # Стандартне додавання і отримання.
    distributed_map.put("key", "value")
    distributed_map.get("key")
    # Конкурентні методи мапи, оптимістичне оновлення.
    distributed_map.put_if_absent("somekey", "somevalue")
    distributed_map.replace_if_same("key", "value", "newvalue")
    # Вимкнення цього клієнта Hazelcast.
    client.shutdown()