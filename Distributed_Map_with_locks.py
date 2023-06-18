from hazelcast.client import HazelcastClient
from hazelcast.lock import LockService

# Створення клієнта Hazelcast
client = HazelcastClient()

# Отримання розподіленої мапи з клієнта
map = client.get_map("my-distributed-map")

# Приклад без блокування
def example_without_lock():
    for i in range(10):
        map.put(i, i)

# Приклад з песимістичним блокуванням
def example_with_pessimistic_lock():
    lock_service = client.get_lock_service()
    lock = lock_service.get_lock("my-lock")
    lock.lock()
    try:
        for i in range(10):
            map.put(i, i)
    finally:
        lock.unlock()

# Приклад з оптимістичним блокуванням
def example_with_optimistic_lock():
    lock_service = client.get_lock_service()
    lock = lock_service.get_lock("my-lock")
    while True:
        lock.lock()
        try:
            # Перевірка, що ніхто інший не змінює мапу
            if map.get_size() == 0:
                for i in range(10):
                    map.put(i, i)
                break
        finally:
            lock.unlock()

# Запуск прикладів на різних клієнтах або підключеннях
example_without_lock()
example_with_pessimistic_lock()
example_with_optimistic_lock()

# Отримання результатів
result_without_lock = map.get_size()
print("Розмір мапи без блокування:", result_without_lock)

result_with_pessimistic_lock = map.get_size()
print("Розмір мапи з песимістичним блокуванням:", result_with_pessimistic_lock)

result_with_optimistic_lock = map.get_size()
print("Розмір мапи з оптимістичним блокуванням:", result_with_optimistic_lock)

# Закриття клієнта
client.shutdown()
