import thread
import socket
import vals

for i in range(vals.number_of_threads):
    x = thread.thread(i)
    x.start()

while True:
    if not("running" in vals.threads_status):
        for i in vals.available_ips:
            try:
                hostname = gethostbyaddr(i)
            except:
                hostname = "-"
            print("[ " + i + " ]    " + hostname)
        break
