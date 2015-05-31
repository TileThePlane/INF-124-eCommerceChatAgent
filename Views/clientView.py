#printStuff
from Controllers import messageFetcher

name = ""

def startClient():
  print messageFetcher.fetchMessage(0)
  global name
  name = raw_input(messageFetcher.fetchMessage(1)).rstrip()
  print (messageFetcher.fetchMessage(2) + name)
  menuSelection = "0"
  while menuSelection == "0":
    menuSelection = raw_input(messageFetcher.fetchMessage(3)).rstrip()
    if menuSelection == "1":
      print(messageFetcher.fetchMessage(4) + "Order shirts")
    elif menuSelection == "2":
      print(messageFetcher.fetchMessage(4) + "Questions")
    elif menuSelection == "3":
      print(messageFetcher.fetchMessage(4) + "Complaints")
    else:
      menuSelection = "0"
  print(messageFetcher.fetchMessage(5))
  return {'name': name, 'selection': menuSelection}
def getUserInput():
  global name
  mytxt = raw_input().rstrip()
  return mytxt
def processMessage(msg):
  print("Agent " + msg['speak'] + ": " + msg["txt"])
def connectionClosed():
  print 'Connection to Server Lost. Quitting'
def processInput(selection):
  if selection == 0:
    print 'quitting'
  elif selection == 1:
    print 'saving a log file'
  elif selection == 2:
    print(messageFetcher.fetchMessage(8))
def processNetworkSettings():
  host = raw_input("Enter host IP address: ")
  port = int(raw_input("Enter Port #:"))
  return {"host": host, "port": port}