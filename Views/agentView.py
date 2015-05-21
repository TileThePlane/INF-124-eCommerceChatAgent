#printStuff
import sys


name = ""

def startClient():
  print 'Welcome'
  global name
  name = raw_input('What is your name? ').rstrip()
  return name
def getUserInput():
  global name
  mytxt = raw_input(name + ': ').rstrip()
  return mytxt