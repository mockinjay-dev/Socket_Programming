import socket

#loop_back_IP
tcp_ip='127.0.0.1'
tcp_port=5005
buffer_size=1024

#AF_INET=Address Family Internet
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((tcp_ip,tcp_port))
s.listen(1)
conn,addr=s.accept()
print('Connection Addres:',addr)
while 1:
	data=conn.recv(buffer_size)
	if not data:
		break
	print("Bob_Vikash:",data.decode())
	data=input("Tintin:")
	conn.send(bytes(data,'utf-8'))
conn.close()
s.close()

