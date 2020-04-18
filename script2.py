import time
import threading

start = time.perf_counter()

def connect():
    print("connecting to  192.168.1.1")
    time.sleep(2)
    print("done configuring 192.168.1.1")


t1 = threading.Thread(target=connect)
t2 = threading.Thread(target=connect)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")