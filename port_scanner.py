import socket, threading, queue

target = "127.0.0.1"
queue = queue.Queue()
open_ports = []

def port_scan(port):
        try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
                return True
        except:
                return False

# for port in range(1, 1024):
#         result = port_scan(port)

#         if result:
#                 print("Port {} is open".format(port))
#         else:
#                 print("Port {} is closed".format(port))
#
# -- scanning one by one

def fill_queue(port_list):
        for port in port_list:
                queue.put(port)

def worker():
        while not queue.empty():
                port = queue.get()

                if port_scan(port):
                        # print("Port {} is open".format(port))
                        open_ports.append(port)
                # else: 
                        # print("Port {} is closed".format(port))

port_list = range(1, 1025)
fill_queue(port_list)

thread_list = []

for t in range(512):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

for thread in thread_list:
        thread.start()

for thread in thread_list:
        thread.join()

# -- scanning usign multithreading

print("Open Ports: ", open_ports)