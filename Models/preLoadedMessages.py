messages = ["Welcome to Socks and Shirts!", #Code: 0
 "What is your name? ", #Code: 1
 "Thank you, ", #Code: 2
 "How can we assist you today?\n\t1) Order shirts\n\t2) Questions\n\t3) Complaints\n", #code 3
 "Your selection was: ", #Code: 4
 "Connecting you with an agent, please wait", #code5
 "Welcome, Agent.\nWhat is your name?", #code6
 "Waiting on a client", #code7
 '''MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMNNMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNN7,,,,,ZNNNMMMMMMMMMMMMMMMMMMNNNMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNN~,,,,,,,,,,,,,,,NNMMMMMMMMMMMMMMMMNNNNMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNN8,,,,,,,,NNNNI=ONNN,,,NNMMMMMMMMMMMMMMNN,NMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNN,,,,,,,,NN,,,=NNNNN,,,N,,8NMMMMMMMMMMMMMN,,NNMM
 MMMMMMMMMMMMMMMMMMMMMMMMMNNNNZ,,,,,,,,NNN,NNNNNNNNNNNNNN,O$NNMMMMMMMMMMMND,,,NMM
 MMMMMMMMMMMMMMMMMMMMMN,,N,,,,O,,,8NNNNNNNNNNNNNNNNNNNNNNNN,,NNMMMMMMMMMNN,,,,NNM
 MMMMMMMMMMMMMMMMMMMMNN,,,,N,NI,,,,,,,,NNNNNNNNNNNNNNNNNNNNN+,NNMMMMMMMND,,,,,,NM
 MMMMMMMMMMMMMMMMMMNN,,,,,,,,,,,,,,,,,,,8NNNNNNNNNNNNN,,,,,,,,,NNNNNNNN,,,,,,,,NN
 MMMMMMMMMMMMMMMMNN,,,,,,NNNN,,,?,,,?N8,,,,NNNNNNNN$,,=,,,,,,,,N,,,,,,,,,,,,,,,NN
 MMMMMMMMMMMMMMMNN,I,NN,NNN,,,,,,,,,,,,,,~,,,NNNNN,,I,,,,,,,,,,N,,,,,,,,,,,,,,,NN
 MMMMMMMMMMMMMNN,,,,,,ZI,,,,,,,,,,,,,,,,,,,,,,NN~,,N,,,,,,,,,,NN,,,,,,,,,,,,,,,NN
 MMMMMMMMMMMNN,,,,,,,,,,,,,,,,,,I,N,,,,,,,,,,,NI,,N:,,,,,,,,,,,N,,,,,,,,,,,,,,,NN
 MMMMMMMMMNN,,,,,,,,,,,,,,,,,,N,,,,,,,,,,,,,,,N,,ZN,,,,,,,,,,D,N,,,,,,,,,,,,,,,NM
 MMMMMMMNN,,,,,,,,,,,,,,NNNNO,,,,~,,,,,,,,,,=Z,,NNN,,,,,,,,,,,NN,,,,,,,,,,,,,,NNM
 MMMMMNN,,,,,,,,,,DNNNMMMMMN,I,,,I,,,,,,,,,,N,,NNNN,,,,,,,,,,,NN,,,,,,,,,,,,,,NNM
 MMMNN,,,,,,,,NNNMMMMMMMMMMN,,,~,,,,,,,,,,,INNNNN+N?,,,,,,,,,NNNN,,,,,,,,,,,,NNMM
 MMN:,,,,,8NNMMMMMMMMMMMMMMMNN,,,,,,,,,,,,,NNNNN,,,NN,,,,,,,,,,NNN,,,,,,,,,,NNMMM
 NN,,,,7NNMMMMMMMMMMMMMMMMMMN:,,,,,~,,,,,,NNNN$,,,NMNNN,,,,,,,,NMNN,,,,,,,,NNMMMM
 ,,,,NNMMMMMMMMMMMMMMMMMMMMMMNO,,,,,ND,,,,,N,,,,,,DNMMNN~,,,,,,NNMNNN,,,,INNMMMMM
 N7NNMMMMMMMMMMMMMMMMMMMMMMMMN,,,,,N,,,,,,,N,,,,,,NMMMMMN,,,,,,,NMMMNNNNNNMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMN,,,,,:,,,,,,,N=,,,$,,,NMMMNN,,,,,,,,NNMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMNN,,N,O,,,,,,,=NI,,N,NNMMMNO,D,,,,,,,NNMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNN8,,,,,,,,NMMMMMMMMMMMNO~,,NDNNNMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:,,,,,,,,NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM?,,,,,,,,,INMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNN,,,,,,,~NNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'''
 ] #code 8
 
 
def getPreloadedMessages(messageCode):
 global messages
 return messages[messageCode]
