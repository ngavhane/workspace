import socket
def main():
    host="127.0.0.1"
    port=5008
    s=socket.socket()
    s.connect((host,port))
    message=raw_input("->")
    while message!="q":
        s.send(message)
        data=s.recv(1024)
        print "Data recieved from server side",str(data)
        message=raw_input("->")
    s.close()
main()

