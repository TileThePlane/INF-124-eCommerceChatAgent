

def writingToFileClient( str ):
		f = open('chatlog.txt','a')
		text = 'Client: ' + str + '/n'
		f.write(text)
		f.close()
		
		
def writingToFileAgent( str ):
		f = open('chatlog.txt','a')
		text = 'Agent: ' + str + '/n'
		f.write(text)
		f.close()
	
