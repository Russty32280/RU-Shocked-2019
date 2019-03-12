#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)



dt = 0.001
t = np.arange(0.0, 10.0, dt)
s = np.sin(10*t)
noise = np.random.randn(len(t))
s = np.convolve(s, .25*noise)[:len(noise)]  # colored noise



EventThreshold = .05
EventTimes = []

EventFallingEdge = True
EventRisingEdge = False

Events = []

j = 1
k = 0

for i in range(len(s)):
    if s[i] > EventThreshold:
        EventTimes.append(1)
        if EventRisingEdge == False:
            EventRisingEdge = True
            EventFallingEdge = False
            plt.figure(1)
            plt.axvline(x=i*dt, color='g')
            CurrentEvent = []

        CurrentEvent.append(s[i])
    else:
        EventTimes.append(0)
        if EventFallingEdge == False:
            EventFallingEdge = True
            EventRisingEdge = False
            plt.axvline(x=i*dt, color='r')
            Events.append(CurrentEvent)
            j = j + 1
            plt.figure(j)
            plt.plot(CurrentEvent)
            
        

print(Events)

        
plt.figure(1)
plt.plot(t, s)
plt.show()
