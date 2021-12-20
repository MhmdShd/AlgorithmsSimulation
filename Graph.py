# function to draw graphs for the simulation part

import matplotlib.pyplot as plt
import json
import numpy as np

def Plot():
    file = open('Simulation-algo.txt','r')
    data = json.loads(file.read())


    size = []
    Insertion =[]
    Merge =[]
    Heap =[]
    Quick =[]
    Bubble =[]
    Selection =[]
    Counting =[]

    for i in range(len(data['Simulation Details'])):
        size.append(float(data['Simulation Details'][i]['Size']))
        Insertion.append(float(data['Simulation Details'][i]['Insertion Sort'][0:5]))
        Merge.append(float(data['Simulation Details'][i]['Merge Sort'][0:5]))
        Heap.append(float(data['Simulation Details'][i]['Heap Sort'][0:5]))
        Quick.append(float(data['Simulation Details'][i]['Quick Sort'][0:5]))
        Bubble.append(float(data['Simulation Details'][i]['Bubble Sort'][0:5]))
        Selection.append(float(data['Simulation Details'][i]['Selection Sort'][0:5]))
        Counting.append(float(data['Simulation Details'][i]['Counting Sort'][0:5]))

    _Insertion = np.array(Insertion)
    _Merge = np.array(Merge)
    _Heap = np.array(Heap)
    _Quick = np.array(Quick)
    _Bubble = np.array(Bubble)
    _Selection = np.array(Selection)
    _Counting = np.array(Counting)
    _size = np.array(size)


    plt.plot(_size, _Quick, label='Quick')
    plt.plot(_size, _Bubble, label='Bubble')
    plt.plot(_size, _Selection, label='Selection')
    plt.plot(_size, _Counting, label="Counting")
    plt.plot(_size, _Insertion, label='Insertion')
    plt.plot(_size, _Merge, label='Merge')
    plt.plot(_size, _Heap, label='Heap')
    plt.xlabel('size')
    plt.ylabel("Duration (ms)")
    plt.title("Different Sorting Algorithms")
    plt.legend()
    plt.show()
Plot()