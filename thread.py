import threading
import socket
import vals

class thread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self, target = self.process, args=[])
        self.number = number
        vals.threads_status[self.number] = "running"

    def process(self):
        while True:
            iterate = vals.iterate
            if iterate<255:
                vals.iterate+=1
                current_ip = vals.ip_pre + str(iterate)
                #print("Now at " + current_ip + "\n")
                try:
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.settimeout(vals.timeout)
                    client_socket.connect((current_ip, 5555))
                    client_socket.close()
                    #print("Available IP found: " + current_ip + "\n")
                    vals.available_ips.append(current_ip)


                except ConnectionRefusedError:
                    client_socket.close()
                    #print("Available IP found: " + current_ip + "\n")
                    vals.available_ips.append(current_ip)


                except socket.timeout:
                    #print("Tried " + current_ip + " ==> no success\n")
                    client_socket.close()
            else:
                vals.threads_status[self.number] = "terminated"
                break
        
