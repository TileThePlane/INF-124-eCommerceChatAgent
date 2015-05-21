import sys
sys.path.append("../Models")

import preLoadedMessages

def fetchMessage(messageCode):
  return preLoadedMessages.getPreloadedMessages(messageCode)