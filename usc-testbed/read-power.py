with open('normal-rpl-v3/power.txt', 'r') as f:
	for line in f.readlines():
		data = line.split()
		print data[9]