from hazelcast.client import HazelcastClient

# Підключення до кластера Hazelcast
client = HazelcastClient()

# Отримання розподіленої мапи
distributed_map = client.get_map("my-distributed-map")

# Запис 1000 значень в розподілену мапу
for i in range(1000):
    key = str(i)
    value = "Value " + str(i)
    distributed_map.put(key, value)

# Закриття з'єднання з кластером Hazelcast
client.shutdown()
