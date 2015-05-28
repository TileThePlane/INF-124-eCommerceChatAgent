import sys


messages = ["Welcome to Socks and Shirts!", #Code: 0
 "What is your name? ", #Code: 1
 "Thank you, ", #Code: 2
 "How can we assist you today?\n\t1) Order shirts\n\t2) Questions\n\t3) Complaints\n", #code 3
 "Your selection was: ", #Code: 4
 "Connecting you with an agent, please wait", #code5
 "Welcome, Agent.\nWhat is your name?", #code6
 "Waiting on a client", #code6
 ] #code 5
def getPreloadedMessages(messageCode):
 global messages
 return messages[messageCode]
