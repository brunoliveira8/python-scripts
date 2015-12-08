with open('final-results/balanced-rpl-80-12/power.txt', 'r') as f:
	for line in f.readlines():
		data = line.split()
		print data[3]