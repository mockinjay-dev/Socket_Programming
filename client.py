import socket

#loop_back_IP
tcp_ip='127.0.0.1'
tcp_port=5005
buffer_size=1024

#AF_INET=Address Family Internet
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((tcp_ip,tcp_port))
for i in range(1,11,1):
	message=input("Bob_Vikash:")
	s.send(bytes(message,'utf-8'))
	data=s.recv(buffer_size)
	print("Tintin:",data.decode())
s.close

