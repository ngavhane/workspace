import time
from threading import Thread
def printTime(name,delay,repeat):
    print "Thread whose name="+name+" started/n"
    while repeat>0:
        time.sleep(2)
        print "Time="+str(time.ctime(time.time()))+" which is printed by thread name="+name
        repeat-=1
    print "Thread with name="+name+" is completed"
def main():
    t1=Thread(target=printTime,args=("nitin",2,5))
    t2=Thread(target=printTime,args=("Sadaanand",2,5))
    t1.start()
    t2.start()
    print "Main function is completed Now"
if __name__=="__main__":
    main()
        
    