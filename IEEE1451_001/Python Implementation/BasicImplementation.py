#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import time

dt = 0.001
t = np.linspace(0.0, 10.0, 10000)
s = np.sin(2*np.pi*t)

SignalPosition = 0



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
            #print(row)
            Temperatures.append(float(row[0]))

#print(Temperatures)

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
            #print(row)
            Accelerometers.append(float(row[1]))

#print(Accelerometers)

plt.stem(Accelerometers)
plt.show()





S = 0
Tempos = [0]
Class = ['']
Mark = [0]
J = 0
K = 0

N = 48
Err = 30

Signal = np.zeros(52)

Up = 0
Down = 0
Equal = 0




def ReadADC():
    global SignalPosition
    CurrentReading = Accelerometers[SignalPosition]
    SignalPosition = SignalPosition + 1
    return CurrentReading

InitialReading = ReadADC()
Signal[0] = InitialReading
Mark = [InitialReading]

def InitializeSegmentCounters():
    global K
    global J
    global Up
    global Down
    global Equal
    K = 0
    J = 0
    Up = 0
    Down = 0
    Equal = 0





def DetermineSegment():
    global SignalPosition, Up, Down, Equal, S, Err, J, K
    J = J + 1
    K= K + 1
    Signal[K] = ReadADC()
    K = K + 1
    Signal[K] = ReadADC()
    Diff = (Signal[0]+Signal[K])/2 - Signal[J]
    if Diff > 0:
        Up = Up + 1
    elif Diff < 0:
        Down = Down + 1
    else:
        Equal = Equal + 1

    if K >= N:
        if Signal[0] == Signal[K]:
            Class.append('a')
        elif Signal[0] < Signal[K]:
            Class.append('b')
        else:
            Class.append('c')
        Mark.append(Signal[K])
        print("Tempos: ", Tempos[S])
        print("K ", K)
        Tempos.append(Tempos[S] + K)
        print("New Tempos: ", Tempos[S+1])
        S = S + 1
        Signal[0] = Signal[K]
        print(Mark)
            
    else:
        if abs(Diff) > Err:
            if Up>Down:
                if Signal[0] > Signal[K]:
                    Class.append('f')
                elif Signal[0] < Signal[K]:
                    Class.append('d')
            elif Up<Down:
                if Signal[0] > Signal[K]:
                    Class.append('e')
                elif Signal[0] < Signal[K]:
                    Class.append('g')
            else:
                Class.append('h')
            Mark.append(Signal[K])
            Tempos.append(Tempos[S] + K)
            S = S + 1
            Signal[0] = Signal[K]
            #print(Mark)
            #print(s[SignalPosition])
        else:
            DetermineSegment()
            InitializeSegmentCounters()


InitializeSegmentCounters()
for i in range(100):
    DetermineSegment()
    


print(Class)
#print(Tempos)
#print(Mark)
            
for time in Tempos:
    print(time)
    plt.axvline(x=time, color='r')

plt.plot(Accelerometers)

for i in range(5):
    print(Mark[i])
    plt.axhline(y=Mark[i], color='g')

plt.show()
