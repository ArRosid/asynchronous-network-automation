import time
import threading


PARALEL_COUNT = 3

start = time.perf_counter()

ip_list = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3', 
            '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', 
            '192.168.1.8', '192.168.1.9']

ip_list_group = []
for i in range(0,len(ip_list),PARALEL_COUNT):
    ip_list_group.append(ip_list[i:i+PARALEL_COUNT])

# print(ip_list_group)

def connect(ip):
    print(f"connecting to  {ip}")
    time.sleep(2)
    print(f"done configuring {ip}")

threads = []
for ip_list in ip_list_group:
    for ip in ip_list:
        t = threading.Thread(target=connect, args=[ip])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")