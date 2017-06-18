#!/bin/bash

#Executes youCaught.py three times over one minute.

for i in 1 2 3;
do
	python /home/pi/everyFish/youCaught.py
	/bin/sleep 20
done
