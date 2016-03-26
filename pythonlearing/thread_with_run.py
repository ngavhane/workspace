import time
from threading import Thread
class AsyncWrite(Thread):
    def __init__(self,text,filename):
        Thread.__init__(self)
        self.text=text
        self.Filename=filename
    def run(self):
        fileobj=open(self.Filename,"w")
        fileobj.write(self.text+"\n")
        fileobj.close()
        time.sleep(2)
        print "Background writing to a file  with name ="+self.Filename+"has been finished"
def Main():
    classobj=AsyncWrite("My name is nitin ashokrao gavhane","out.text")
    classobj.start()
    print "Program is continue to run while write operation is still running running in background"
    print "look math is also working",(400+500)
    #classobj.join()
    print "Waited untill thread finishes it's execution"
if __name__=="__main__":
    Main()