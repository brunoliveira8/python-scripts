
nodes = [1]

FLAG = 1


def main():
	last_sent,last_fw,last_rcv,last_sw = [0,0,0,0]
	if FLAG == 0:
		for node in nodes:
			with open('final-results/balanced-rpl-80/mote{}.txt'.format(node), 'r') as f:
				lines = f.readlines()
				for x in xrange(4):
					with open('final-results/balanced-rpl-80-{}/mote{}.txt'.format(x+5,node), 'w') as f1:
						for y in xrange(120):
							
							if x == 0:
								f1.write(lines[x*120+y])

							else:
								tx, rx, sent, fw, rcv, sw = lines[x*120+y].split() 
								sent = int(sent) - last_sent
								fw = int(fw) - last_fw
								rcv = int(rcv) - last_rcv
								sw = int(sw) - last_sw
								f1.write("{} {} {} {} {} {} \n".format(tx, rx, sent, fw, rcv, sw))

							if y == 119:
								last_line = lines[x*120+y]
								last_sent,last_fw,last_rcv,last_sw =  last_line.split()[2:]
								last_sent = int(last_sent) 
								last_fw = int(last_fw)
								last_rcv = int(last_rcv)
								last_sw = int(last_sw)


	else:
			for node in nodes:
				with open('final-results/balanced-rpl-80-v4/mote{}.txt'.format(node), 'r') as f:
					lines = f.readlines()
					for x in xrange(2):
						with open('final-results/balanced-rpl-80-{}/mote{}.txt'.format(x+11,node), 'w') as f1:
							for y in xrange(120):
							
								if lines[x*120+y].split()[0] == '#1':
								
									if x == 0:
										f1.write(lines[x*120+y])

									else:
										tx, rx, sent, fw, rcv = lines[x*120+y].split()[1:] 
										sent = int(sent) - last_sent
										fw = int(fw) - last_fw
										rcv = int(rcv) - last_rcv
								
										f1.write("#1 {} {} {} {} {} \n".format(tx, rx, sent, fw, rcv))

									if y == 119:
										last_line = lines[x*120+y]
										last_sent,last_fw,last_rcv =  last_line.split()[3:]
										last_sent = int(last_sent) 
										last_fw = int(last_fw)
										last_rcv = int(last_rcv)
										



					

	
	             



if __name__ == '__main__':
	main()