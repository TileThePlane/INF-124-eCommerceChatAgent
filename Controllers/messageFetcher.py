import Models.preLoadedMessages
from Models import preLoadedMessages
def fetchMessage(messageCode):
  return preLoadedMessages.getPreloadedMessages(messageCode)
