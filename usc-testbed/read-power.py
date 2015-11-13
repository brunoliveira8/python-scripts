with open('balanced-rpl10/power.txt', 'r') as f:
	for line in f.readlines():
		data = line.split()
		print data[9]