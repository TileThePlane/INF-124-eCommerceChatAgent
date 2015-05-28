from network import Handler, poll
import sys
from threading import Thread
from time import sleep

sys.path.append("../Views")

import agentView

clientName = ""

def processClientJoin(msg):
    global clientName
    clientName = msg["join"]
    clientSelection = msg["selection"]
    if clientSelection == "1":
        clientSelection = "Ordering Shirts"
    elif clientSelection == "2":
        clientSelection = "Questions"
    elif clientSelection == "3":
        clientSelection = "Complaints"
    print("\n==============================")
    print("Client name: " + clientName + "\nSelection: " + clientSelection)
    print("==============================")
def processClientMessage(msg):
    print("\nClient " + msg['speak'] + ": " + msg["txt"])
    

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
            if 'join' in msg.keys():
                processClientJoin(msg)
            elif 'speak' in msg.keys():
                processClientMessage(msg)
            #print msg
        
host, port = 'localhost', 8889
client = Client(host, port)

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
    #client.do_send({'join' : myname})
    client.do_send({'speak': myname, 'txt': mytxt, 'type':'2'})
    sleep(1)
