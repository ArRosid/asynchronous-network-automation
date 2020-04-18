# for n in range(10):
#     print(n)

# # start, stop, step
# for n in range(1,10,2):
#     print(n)

import json


ip_list = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3', 
            '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', 
            '192.168.1.8', '192.168.1.9']


# # print(ip_list[0:3])

ip_list_baru = []

for n in range(0,len(ip_list),5):
    # print(ip_list[n:n+5])
    ip_list_baru.append(ip_list[n:n+5])


# print(ip_list_baru)
print(json.dumps(ip_list_baru, indent=3))
# ip_list_baru = [
#     ["192.168.1.0", "192.168.1.1", "192.168.1.2"],
#     ["192.168.1.3", "192.168.1.4", "192.168.1.5"]
# ]