from network import Listener, Handler, poll
import sys
from time import sleep
handlers = {}  # map client handler to user name
counter=0
class MyHandler(Handler):
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        #sleep(2)
        if 'speak' in msg.keys():
            for i in handlers.keys():
                if i!=self.name:
                    handlers[i].do_send(msg)
        elif 'join' in msg.keys():
            print(counter,msg['join'] + ' has connected.')
            if msg['type'] == '1':
                print("Client connected")
            else:
                print("Agent connected")

            handlers[msg['join']] = self
            self.name = msg['join']
            print(self.name)
            print(handlers)
        else:
            print(counter,msg)
            
 
 
port = 8889
server = Listener(port, MyHandler)
print 'Chat Server Started!'
while 1:
    poll(timeout=0.05) # in seconds
