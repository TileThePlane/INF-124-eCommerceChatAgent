from network import Handler, poll
import sys
from threading import Thread
from time import sleep

sys.path.append("../Views")

import agentView

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
            print msg
        
host, port = 'localhost', 8889
client = Client(host, port)

myname = agentView.startClient()
client.do_send({'join': myname})

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    mytxt = agentView.getUserInput()
    client.do_send({'speak': myname, 'txt': mytxt})
    sleep(1)
