import time
import threading

start = time.perf_counter()

def connect(ip):
    print(f"connecting to  {ip}")
    time.sleep(2)
    print(f"done configuring {ip}")


threads = []
for n in range(10):
    t = threading.Thread(target=connect, args=["192.168.1.10"])
    t.start()
    threads.append(t)

# print(threads)
for t in threads:
    t.join()

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")