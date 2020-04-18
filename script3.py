import time
import threading

start = time.perf_counter()

def connect():
    print("connecting to  192.168.1.1")
    time.sleep(2)
    print("done configuring 192.168.1.1")


threads = []
for n in range(20):
    t = threading.Thread(target=connect)
    t.start()
    # t.join()
    threads.append(t)

print(threads)

for t in threads:
    t.join()

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")