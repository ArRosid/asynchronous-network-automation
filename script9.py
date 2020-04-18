import paramiko
import time
import threading


PARALEL_COUNT = 3

start = time.perf_counter()

ip_list = ["192.168.122.12","192.168.122.85",'192.168.122.158',
            "192.168.122.51","192.168.122.231"]


ip_list_group = []
for i in range(0,len(ip_list),PARALEL_COUNT):
    ip_list_group.append(ip_list[i:i+PARALEL_COUNT])

# print(ip_list_group)

def connect(ip,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username, password=password, look_for_keys=False)

    print ("Success login to {}".format(ip))
    conn = ssh_client.invoke_shell()

    conn.send("terminal length 0\n")
    conn.send("show run\n")
    time.sleep(10)

    output = conn.recv(65535).decode()
    
    file_ = open(f"asyn_backup/{ip}.cfg","w")
    file_.write(output)
    file_.close()

    ssh_client.close()


threads = []
for ip_list in ip_list_group:
    for ip in ip_list:
        t = threading.Thread(target=connect, args=[ip,'cisco','cisco'])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")