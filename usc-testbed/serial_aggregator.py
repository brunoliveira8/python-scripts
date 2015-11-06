# Imports
import serial
import sys
import threading


# List with all nodes IDs that are working

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 
		18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
		31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 
		44, 45, 46, 47,48, 49]


'''
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 
		18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32]
'''


def listen_node(node):

	ser = serial.Serial(
		    port='/dev/ttyUSB' + str(node-1), \
		    baudrate=115200, \
		    parity=serial.PARITY_NONE, \
		    stopbits=serial.STOPBITS_ONE, \
		    bytesize=serial.EIGHTBITS, \
		    timeout=1)

	ser.flushInput()
	ser.flushOutput()

	while True:
		with open('data/mote{}.txt'.format(node), 'a') as f:
			data_raw = ser.readline()	
			if len(data_raw) > 0:
				f.write(data_raw)


def main():
	
	threads = []
	for node in nodes:
	    t = threading.Thread(target=listen_node, args=(node,))
	    threads.append(t)
	    t.start()


if __name__ == '__main__':
	main()