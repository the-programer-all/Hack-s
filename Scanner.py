import socket
from IPy import IP

ip_add = input("\n[=]target ip : ")

port = input("\n[=]port to be scanned : ")

def Cheak_IP(ip):
    try:
        if(IP(ip)):
            return ip
    except ValueError:
        try:
            return socket.gethostbyname(ip)
        except Exception as e:
            print(e)

def Get_Banner(sock):
	try:
		sock.settimeout(1)
		return sock.recv(1024).decode()
	except Exception as e:
		pass

def Scan(ip , port):
    sock = socket.socket()
    try:
        cip = Cheak_IP(ip)
        sock.connect((cip , int(port)))
        try:
        	banner = Get_Banner(sock)
        	print("\n[!!]open port " + str(port) + " : " + str(banner.strip("\n")))
        except:
        	print("\n[!!]open port " + str(port))
    except Exception as e:
    	pass

Scan(ip_add , port)
