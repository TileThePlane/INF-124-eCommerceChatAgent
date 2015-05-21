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
        global counter
        if 'speak' in msg.keys():
            counter+=1
            print(counter,msg['speak']+': '+msg['txt'])
            if msg['txt']=='ping':
                self.do_send('pong')
                print('they said ping')
        elif 'join' in msg.keys():
            print(counter,msg['join'] + ' has connected.')
        else:
            print(counter,msg)
 
 
port = 8889
server = Listener(port, MyHandler)
print 'Chat Server Started!'
while 1:
    poll(timeout=0.05) # in seconds
