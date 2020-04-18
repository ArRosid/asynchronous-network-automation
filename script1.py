import time

def connect():
    print("connecting to  192.168.1.1")
    time.sleep(2)
    print("done configuring 192.168.1.1")

start = time.perf_counter()

connect()
connect()
connect()

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")