import http.client

#53
SERVER_IP = '192.168.43.52'
def SendMessage(mess, user, reciver):
	res = http.client.HTTPConnection(SERVER_IP+'/'+mess+'?'+user+'?'+reciver)
	return res.read()
def ReciveMessage(user):
	res = http.client.HTTPConnection(SERVER_IP+'/'+user)
	return res.read()

	
SendMessage('pluje syfem 123','wojtek','hubert')
ReciveMessage('hubert')