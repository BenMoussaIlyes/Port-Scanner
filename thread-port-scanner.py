import threading
import socket 
import time
import multiprocessing as mp
results=[]
def is_port_open(host ,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        results.append(port)
threads = []
host = input("Host : ")

for i in range(0, 1024):
    thread = threading.Thread(target = is_port_open, args = (host,i ))
    threads.append(thread)
    thread.start()
for thread in threads:
        thread.join()

print("open ports:")
for port in results:
		print("--> "+ str(port))
