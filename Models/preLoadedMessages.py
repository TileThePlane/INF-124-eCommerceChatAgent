import sys

messages = ["Welcome!", #Code: 0
 "What is your name? "] #Code: 1

def getPreloadedMessages(messageCode):
 global messages
 return messages[messageCode]
