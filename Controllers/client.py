from network import Handler, poll
import sys
from threading import Thread
from time import sleep

from Views import clientView

log = ""
def writeLog(input):
	global log
	log += "\n"+input


def processAgentMessage(msg):
    print("Agent " + msg['speak'] + ": " + msg["txt"])
    writeLog("Agent " + msg['speak'] + ": " + msg["txt"])

class Client(Handler):
    
    def on_close(self):
        pass
    
    def on_msg(self, msg):
        #print 'message was:'+ str(msg) + '\n'
        if msg==type(str):
            if msg=='pong':
                print 'pong'
                #self.do_send({'speak': myname, 'txt': 'ping'})
        else:
            if 'speak' in msg.keys():
                processAgentMessage(msg)
        
host = raw_input("Enter host IP address: ")
port = int(raw_input("Enter Port #:"))
client = Client(host, port)

clientInfo = clientView.startClient()

myname = clientInfo['name']
clientSelection = clientInfo['selection']

client.do_send({'join': myname, 'selection': clientSelection, 'type':'1'})

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

def writeToFile( str ):
		f = open('chatlog.txt','a')
		f.write(str)
		f.close()


while 1:
    mytxt = clientView.getUserInput()
    writeLog("Client " + myname + ": " + mytxt)
    if mytxt==":q":
        print 'quitting'
        client.do_close()
        break
    elif mytxt==":s":
        print 'saving a log file'
        writeToFile(log)
    else:
        client.do_send({'speak': myname, 'txt': mytxt, 'type':'1'})
        sleep(1)
