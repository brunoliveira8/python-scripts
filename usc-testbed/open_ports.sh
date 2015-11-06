#!/bin/bash
mote=1
for mote in `seq 1 50`;
do
	echo "Opening port ${mote}"
	port=$(($mote-1))
	if [ $mote -ge 10 ]; then
		socat PTY,link=/dev/ttyUSB${port},raw TCP4:testbed.usc.edu:100${mote} &
	else
		socat PTY,link=/dev/ttyUSB${port},raw TCP4:testbed.usc.edu:1000${mote} &
	fi
done 
