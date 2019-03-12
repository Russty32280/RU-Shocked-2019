#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.linspace(0.0, 10.0, 1000)
s = np.sin(2*np.pi*t)

SignalPosition = 0




S = 0
Tempos = [0]
Class = ['']
Mark = [0]
J = 0
K = 0

N = 30
Err = 0.1

Signal = [0]

Up = 0
Down = 0
Equal = 0




def ReadADC():
    global SignalPosition
    CurrentReading = s[SignalPosition]
    SignalPosition = SignalPosition + 1
    return CurrentReading

InitialReading = ReadADC()
Signal = [InitialReading]
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
    global SignalPosition
    global J
    J = J + 1
    global K
    K= K + 1
    global Up, Down, Equal, S
    Signal.append(ReadADC())
    SignalPosition = SignalPosition + 1
    K = K + 1
    Signal.append(ReadADC())
    print('Signal: %d', Signal)
    Diff = (Signal[0]+Signal[K])/2 - Signal[J]
    print('diff: %d', Diff)
    if Diff > 0:
        Up = Up + 1
    elif Diff < 0:
        Down = Down + 1
    else:
        Equal = Equal + 1

    if K == N:
        if Signal[0] == Signal[K]:
            Class.append('a')
            print('a')
        elif Signal[0] < Signal[K]:
            Class.append('b')
            print('b')
        else:
            Class.append('c')
            print('c')
        Mark[S] = Signal[K]
        Tempos[S] = Tempos[S-1] + K
        S = S + 1
        Signal[0] = Signal[K]
            
    else:
        if abs(Diff) > Err:
            if Up>Down:
                if Signal[0] > Signal[K]:
                    Class.append('f')
                    print('f')
                elif Signal[0] < Signal[K]:
                    Class.append('d')
                    print('d')
            elif Up<Down:
                if Signal[0] > Signal[K]:
                    Class.append('e')
                    print('e')
                elif Signal[0] < Signal[K]:
                    print(Class)
                    Class.append('g')
                    print('g')
            else:
                Class.append('h')
            Mark.append(Signal[K])
            Tempos.append(Tempos[S-1] + K)
            S = S + 1
            Signal[0] = Signal[K]
        else:
            DetermineSegment()
            InitializeSegmentCounters()


DetermineSegment()
DetermineSegment()
DetermineSegment()
DetermineSegment()
DetermineSegment()


print(Class)
print(Tempos)
print(Mark)
            
    
plt.plot(s)
plt.show()




