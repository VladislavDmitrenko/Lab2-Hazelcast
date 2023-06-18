from hazelcast.client import HazelcastClient

# Створення клієнта Hazelcast
client = HazelcastClient()

# Отримання розподіленої черги з клієнта
queue = client.get_queue("my-distributed-queue")

# Запис значення в чергу
queue.offer("Value 1")

# Читання значення з черги першим читачем
value1 = queue.poll()
print("Читач 1:", value1)

# Читання значення з черги другим читачем
value2 = queue.poll()
print("Читач 2:", value2)

# Запис значення в чергу
queue.offer("Value 2")

# Читання значення з черги першим читачем
value3 = queue.poll()
print("Читач 1:", value3)

# Закриття клієнта
client.shutdown()
