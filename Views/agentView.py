#printStuff
import sys
sys.path.append("../Controllers")

import messageFetcher

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