#printStuff
from Controllers import messageFetcher

name = ""

def startClient():
  global name
  name = raw_input(messageFetcher.fetchMessage(6)).rstrip()
  print(messageFetcher.fetchMessage(2) + "agent " + name)
  print(messageFetcher.fetchMessage(7))
  return name
def getUserInput():
  global name
  mytxt = raw_input().rstrip()
  return mytxt
def processJoin(msg):
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

def processMessage(msg):
  print("Client " + msg['speak'] + ": " + msg["txt"])
def processDisconnect():
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