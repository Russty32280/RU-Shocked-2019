#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

#Initialize Signal
Reconstructed_Signal = 0

# Calculate the Time Base
#dt = 0.1
dt = 0.001

Class = ['b', 'c', 'd', 'e', 'f', 'g']
#Class = ['g', 'g', 'g', 'g', 'e', 'e', 'e', 'e', 'c', 'f', 'f', 'f', 'f', 'd', 'd', 'd', 'b', 'g', 'g', 'g']
#Mark = [0, 88, 144, 194, 240, 286, 334, 386, 452, 554, 618, 670, 718, 764, 810, 860, 918, 1020, 1096, 1150, 1198]
Mark = [1, 50, 30, 90, 40, 10, 80]
Time = [0, 3, 6, 9, 10.5, 19.5, 26.5] * 10
#Time = [0.0, 0.5252216870771345, 0.7863443371291226, 0.9387758647136907, 0.9980361866128443, 0.9744865517646705, 0.8638176980420761, 0.6564027888394625, 0.29677036097065074, -0.3331478013059903, -0.6756191628035089, -0.8765094281456444, -0.9799450573650522, -0.9960913184522086, -0.9295889941435193, -0.7701686612729851, -0.4922252905323145, 0.12596910269829514, 0.5678359863745065, 0.8094415393976601, 0.9473396432391497]

K = 1

for C in Class:
    print(C)
    t_Segment = np.arange(0, Time[K]-Time[K-1], dt)
    A = (Mark[K] - Mark[K-1])/(Time[K] - Time[K-1])
    if C == 'b' or C == 'c':
        Segment_Data = A * t_Segment[:1000] + Mark[K-1]
    elif C == 'd':
        b = np.log(Mark[K]/Mark[K-1])/(Time[K] - Time[K-1])
        A = Mark[K-1]
        Segment_Data = A * np.exp(b*t_Segment)
    elif C == 'e':
        b = np.log(Mark[K-1] - Mark[K])/(Time[K] - Time[K-1])
        Segment_Data = (Mark[K-1]) - np.exp(b*t_Segment)
    elif C == 'f':
        b = -np.log(Mark[K]/(Mark[K-1]-Mark[K]))/(Time[K] - Time[K-1])
        A = Mark[K-1] - Mark[K]
        Segment_Data = Mark[K] + A*np.exp(-b*t_Segment)
    elif C == 'g':
        A = Mark[K]
        b = -np.log(Mark[K-1]/Mark[K])/(Time[K] - Time[K-1])
        Segment_Data = (Mark[K] - A*np.exp(-b*t_Segment)) + Mark[K-1]

        

    
    Reconstructed_Signal = np.append(Reconstructed_Signal, Segment_Data)
    K = K + 1

print(Segment_Data)


"""
Class = 'a'
Mark = [10, 50]
Time = [0, 3]
K = 1
t_Segment = np.arange(0, Time[K]-Time[K-1], dt)


A = (Mark[K] - Mark[K-1])/(Time[K] - Time[K-1])

data1 = A * t_Segment[:1000] + Mark[K-1]

#np.append(Reconstructed_Signal, data1)

Reconstructed_Signal = np.append(Reconstructed_Signal, data1)



# Obtain Mark, Class, and Time for new segment
Class = 'd'
Mark = [50, 150]
Time = [3, 4]
K = 1

# Set the timebase for calculating the segment data
t_Segment = np.arange(0, Time[K]-Time[K-1], dt)


A = (Mark[K] - Mark[K-1])/(Time[K] - Time[K-1])
b = np.log(2)/Time[K]

data2 = A * np.exp(np.log(2)*(t_Segment[:1000])) - A + Mark[K-1]


Reconstructed_Signal = np.append(Reconstructed_Signal, data2)


Class = 'f'
Mark = [150, 0]
Time = [4, 5]
K = 1

# Set the timebase for calculating the segment data
t_Segment = np.arange(0, Time[K]-Time[K-1], dt)


A = (Mark[K] - Mark[K-1])/(Time[K] - Time[K-1])
b = np.log(2)/Time[K]

data3 = A * np.exp(np.log(2)*(t_Segment[:1000])) - A + Mark[K-1]


Reconstructed_Signal = np.append(Reconstructed_Signal, data2)
"""
plt.plot(Reconstructed_Signal)

#plt.axis([0, 2, 1.1*np.min(data1), 1.1*np.max(data1)])
plt.show()

