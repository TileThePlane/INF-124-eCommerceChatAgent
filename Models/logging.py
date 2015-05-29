

def writeToFile( str ):
		f = open('chatlog.txt','a')
		text = 'Client: ' + str + '/n'
		f.write(text)
		f.close()
		
	
	
