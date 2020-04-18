import paramiko
import time

start = time.perf_counter()

ip_list = ["192.168.122.12","192.168.122.85",'192.168.122.158',
            "192.168.122.51","192.168.122.231"]

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
    
    file_ = open(f"syn_backup/{ip}.cfg","w")
    file_.write(output)
    file_.close()

    ssh_client.close()


for ip in ip_list:
    connect(ip,"cisco","cisco")

finish = time.perf_counter()
print(f"finishing on {round(finish-start, 2)} seconds")