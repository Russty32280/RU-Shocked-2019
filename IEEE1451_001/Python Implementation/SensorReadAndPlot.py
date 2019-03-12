#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import csv

Temperatures = []

with open('Temperature_Data1.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    row_count = 0
    for row in reader:
        if row_count < 2:
            row_count = row_count+1
        else:
            print(row)
            Temperatures.append(float(row[0]))

print(Temperatures)

#plt.plot(Temperatures)
#plt.show()


Accelerometers = []

with open('Accelerometer_Data.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    row_count = 0
    for row in reader:
        if row_count < 2:
            row_count = row_count+1
        else:
            print(row)
            Accelerometers.append(float(row[1]))

print(Accelerometers)

plt.stem(Accelerometers)
plt.show()
