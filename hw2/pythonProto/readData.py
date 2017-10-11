#going to open and create the publisher for the data
import time

file = open("simulation.csv", "r")

for line in file:
    if line == "---\n":
        time.sleep(1)
    print line.split(',')