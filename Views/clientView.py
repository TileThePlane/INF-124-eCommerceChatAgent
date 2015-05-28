#printStuff
import sys
sys.path.append("../Controllers")

import messageFetcher

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
  return name
def getUserInput():
  global name
  mytxt = raw_input(name + ': ').rstrip()
  return mytxt