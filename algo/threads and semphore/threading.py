import threading

# Global counter variable
counter = 0

# Create a lock object
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # Using 'with lock' automatically acquires and releases the lock.
        # It ensures that only one thread updates counter at a time.
        with lock:
            counter += 1

threads = []

# Create 5 threads for the increment function.
for _ in range(5):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

# Wait for all threads to finish execution.
for t in threads:
    t.join()

print("Counter (with lock):", counter)
# Expect the counter to be 500000 because every increment is done safely.
