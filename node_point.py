from hazelcast.client import HazelcastClient

# Конфігурація клієнта Hazelcast
config = {
    "cluster_name": "my-cluster",
    "cluster_members": [
        "127.0.0.1:5701",  # Адреса та порт першої ноди
        "127.0.0.1:5702",  # Адреса та порт другої ноди 
    	"127.0.0.1:5703",  # Адреса та порт третьої ноди	
	]
}

# Створення клієнта Hazelcast
client = HazelcastClient(**config)

# Отримання розподіленої мапи з кластеру
distributed_map = client.get_map("capitals")

# Взаємодія з мапою
distributed_map.put("1", "Tokyo")
distributed_map.put("2", "Paris")
distributed_map.put("3", "USA")

# Виведення значень мапи
print(distributed_map.get("1"))
print(distributed_map.get("2"))
print(distributed_map.get("3"))

# Закриття клієнта Hazelcast
client.shutdown()
