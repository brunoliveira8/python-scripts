__author__ = 'pedro'

# Imports
import serial
import time
import datetime
import os
import sys

# List with all nodes IDs
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

# Channels
channels = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# Serial ports
serials = []

#default_dir = sys.argv[1]    # The directory for log files
default_dir = "data"    # The directory for log files

n_nodes = 49

def print_to_file(text, filename, mode):
    " This function prints 'text_to_write' into 'filename'"
    # Extract the directory
    dir = os.path.dirname(filename)
    try:
        # Try to create the directory
        os.makedirs(dir)
    except OSError:
        # If it exists, OK
        if os.path.exists(dir):
            pass
        else:
            # Else, raise an exception
            raise
    # Open file
    f = open(filename, mode)
    if text != "":
        # Write text
        f.write(" " + text)
        # Close file
    f.close()
    return

# Opening two serial ports (COM0 and COM1)
for i in range(n_nodes):
    port = serial.Serial(
        port='/dev/ttyUSB' + str(i), \
        baudrate=115200, \
        parity=serial.PARITY_NONE, \
        stopbits=serial.STOPBITS_ONE, \
        bytesize=serial.EIGHTBITS, \
        timeout=1)
    # Append the open ports in the array
    serials.append(port)
    print "Opened port " + serials[i].portstr

# Starting the experiment
for channel in channels:                                                        # for all channels
    
    print "Channel " + str(channel)


    for sender in nodes:
        print "Sender " + str(sender)
        
        dirpath = default_dir + "/"  + str(channel) + "/" + str(sender)
        
        # If there is no 'done' file, we need to run the experiment
        if not os.path.exists(dirpath + "/done"):
            
            # Reseting all nodes
            for node in nodes:
                serials[node - 1].write("\n")
                serials[node - 1].flushInput()
                serials[node - 1].write("\nlinkquality 1\n")
                serials[node - 1].flush()
                line = serials[node - 1].readline()
                while "Link quality reset" not in line:
                    serials[node - 1].write("\nlinkquality 1\n")
                    serials[node - 1].flush()
                    line = serials[node - 1].readline()
        
            # Transmit 100 packets
            for i in range(100):
    
                print "Sending packet {0}".format(i)
    
                # Send packet on source
                serials[sender - 1].write("\nlinkquality 3 {0}\n".format(i))
                serials[sender - 1].flush()
                serials[sender - 1].flushInput()
                time.sleep(0.05)
    
            for receiver in nodes:
                if receiver != sender:
                    print "Receiver " + str(receiver)
                    # Gather statistics from destination
                    PRR = []
            
                    serials[receiver - 1].write("\n")
                    serials[receiver - 1].flushInput()
                    serials[receiver - 1].write("\nlinkquality 4\n")
                    serials[receiver - 1].flush()
                    line = serials[receiver - 1].readline()
                    while "Statistics:" not in line:
                        serials[receiver - 1].write("\nlinkquality 4\n")
                        serials[receiver - 1].flush()
                        line = serials[receiver - 1].readline()
            
                    # Dump statistics int file
                    filename = dirpath + "/" + str(receiver) + "/rssi.dat"
                    for i in range(100):
                        print_to_file(serials[receiver - 1].readline(), filename, 'a')
            
            # Finished the experiment
            print_to_file("", dirpath + "/done", 'w')
        

