import socket
#This is a TCP server file
#My name is nitin
def Main():
    host="127.0.0.1"
    port=5006
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    c,addres=s.accept()
    print "Connection from :",str(addres)
    while True:
        data=c.recv(1024)
        if not data:
            break
        print "Data received from connected side", str(data)
        datatosent=data.upper()
        print "Sending Capitalized data now"
        c.send(str(data))
    c.close()
if __name__=="__main__":
    Main()
