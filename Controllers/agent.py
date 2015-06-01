from network import Handler, poll
import sys
from threading import Thread
from time import sleep

from Views import agentView
from Models import preLoadedMessages

myname=""
log=""
def writeLog(input):
    global log
    log += "\n"+input

def writeToFile( str ):
    f = open('chatlog.txt','a')
    f.write(str)
    f.close()

class Client(Handler):
    
    def on_close(self):
        agentView.processDisconnect()
        sys.exit(0)
    
    def on_msg(self, msg):
        if msg==type(str):
            if msg=='pong':
                print 'pong'
        else:
            if 'join' in msg.keys():
                agentView.processJoin(msg)
                client.do_send({'speak': myname, 'txt': "has entered chat", 'type':'2'})
            elif 'speak' in msg.keys():
                agentView.processMessage(msg)
        
networkSettings = agentView.processNetworkSettings()
client = Client(networkSettings["host"], networkSettings["port"])

myname = agentView.startClient()
client.do_send({'join': myname, 'type':'2'})

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    mytxt = agentView.getUserInput()
    if mytxt==":q":
        agentView.processInput(0)
        client.do_close()
        break
    elif mytxt==":s":
        agentView.processInput(1)
        writeToFile(log)
    elif mytxt==":e":
        agentView.processInput(2)
    else:
        client.do_send({'speak': myname, 'txt': mytxt, 'type':'2'})
