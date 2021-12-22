from time import sleep
from math import floor


#  Heap Sort

def max_heapify(data, i, size, drawData, speed, visual):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= size - 1 and data[l] > data[i]:
        large = l
    else:
        large = i
    if r <= size - 1 and data[r] > data[large]:
        large = r
    if large != i:
        data[i], data[large] = data[large], data[i]
        max_heapify(data, large, size, drawData, speed, visual)

    # drawing if user chose to
    if visual == True:
        drawData(data, getColorheap(len(data), i, large, l, r))

    sleep(speed)


def build_max_heap(data, drawData, speed, visual):
    size = len(data)
    for i in range(floor(len(data) / 2) - 1, -1, -1):
        sleep(speed)
        max_heapify(data, i, size, drawData, speed, visual)


def heap_sort(data, drawData, speed, visual=False):
    build_max_heap(data, drawData, speed, visual)
    size = len(data)
    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        size = size - 1
        max_heapify(data, 0, size, drawData, speed, visual)


# getting proper color
def getColorheap(datalen, I, large, l, r):
    color = []
    for i in range(datalen):
        if i <= datalen:
            color.append("grey")
        else:
            color.append("white")
        if i == I:
            color[i] = 'green'
        if i == l:
            color[i] = 'blue'
        if i == r:
            color[i] = 'yellow'
    return color


#  Insertion Sort

def insertion_sort(data, drawData, speed, visual=False):
    for j in range(1, len(data)):
        x = data[j]
        i = j - 1
        while i >= 0 and data[i] > x:
            sleep(speed)
            data[i + 1] = data[i]
            i -= 1

            # drawing if user chose to
            if visual == True:
                drawData(data, ['green' if x == j or x == i else 'red' for x in range(len(data))])

        data[i + 1] = x


# Selection Sort

def selection_sort(data, drawData, speed, visual=False):
    for i in range(0, len(data)):
        x = data[i]
        small = i
        sleep(speed)
        for j in range(i, len(data)):
            if data[j] < data[small]:

                # drawing if user chose to
                if visual == True:
                    drawData(data, ['green' if x == j or x == i else 'red' for x in range(len(data))])

                sleep(speed)
                small = j
        data[i], data[small] = data[small], data[i]


# Merge Sort

def merge(data, head, idx, tail, drawData, speed, visual=False):
    n1 = idx - head + 1
    n2 = tail - idx
    left = [0] * len(data)
    right = [0] * len(data)
    for i in range(n1):
        sleep(speed)
        left[i] = data[head + i]

        # drawing if user chose to
        if visual:
            drawData(data, getColor(len(data), head, tail))

    for i in range(n2):
        sleep(speed)
        right[i] = data[idx + i + 1]

        # drawing if user chose to
        if visual:
            drawData(data, getColor(len(data), head, tail))

    left[n1] = float('inf')  # setting the value to infinity
    right[n2] = float('inf')  # setting the value to infinity

    i = 0
    j = 0
    for x in range(head, tail + 1):

        # drawing if user chose to
        if visual:
            drawData(data, getColor(len(data), head, tail))

        if left[i] <= right[j]:
            data[x] = left[i]
            i += 1
        else:
            data[x] = right[j]
            j += 1


def merge_sort(data, head, tail, drawData, speed, visual=False):
    if head < tail:
        idx = floor((head + tail) / 2)
        merge_sort(data, head, idx, drawData, speed, visual)
        merge_sort(data, idx + 1, tail, drawData, speed, visual)
        merge(data, head, idx, tail, drawData, speed, visual)


# getting proper color
def getColor(datalen, head, tail):
    color = []
    for i in range(datalen):
        if i >= head and i <= tail:
            color.append("yellow")
        else:
            color.append("grey")
        if i == tail:
            color[i] = 'blue'
        if i == head:
            color[i] = 'blue'
    return color


# Bubble Sort

def bubble_sort(data, drawData, speed, visual=False):
    for x in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                # drawing if user chose to
                if visual == True:
                    drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])

                sleep(speed)


# Merge Sort

def partition(data, head, tail, drawData, speed, visual=False):
    pivot = data[tail]
    border = head - 1

    # drawing if user chose to
    if visual == True:
        drawData(data, getColorquick(len(data), head, tail, border, border))

    sleep(speed)
    for j in range(head, tail):
        if data[j] <= pivot:

            # drawing if user chose to
            if visual == True:
                drawData(data, getColorquick(len(data), head, tail, border, j, True))

            sleep(speed)
            border += 1
            data[border], data[j] = data[j], data[border]

        # drawing if user chose to
        if visual == True:
            sleep(speed)
            drawData(data, getColorquick(len(data), head, tail, border, j))

    # drawing if user chose to
    if visual == True:
        sleep(speed)
        drawData(data, getColorquick(len(data), head, tail, border, tail, True))

    data[border + 1], data[tail] = data[tail], data[border + 1]

    return border + 1


def quick_sort(data, head, tail, drawData, timeTick, visual=False):
    if head < tail:
        p = partition(data, head, tail, drawData, timeTick, visual)

        quick_sort(data, head, p - 1, drawData, timeTick, visual)
        quick_sort(data, p + 1, tail, drawData, timeTick, visual)


# getting proper color
def getColorquick(datalen, head, tail, border, currId, isSwapping=False):
    color = []
    for i in range(datalen):
        if i >= head and i <= tail:
            color.append("grey")
        else:
            color.append("white")

        if i == tail:
            color[i] = 'blue'
        elif i == border:
            color[i] = 'red'
        elif i == currId:
            color[i] = 'yellow'
        if isSwapping:
            if i == border or i == currId:
                color[i] = 'green'
    return color


# Counting Sort
def counting_sort(data, b, k, drawData, speed, visual=False):
    c = [0] * (k + 1)
    for j in range(0, len(data)):
        x = data[j]
        c[data[j]] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    for j in range(len(data) - 1, -1, -1):
        b[c[data[j]] - 1] = data[j]

        # drawing if user chose to
        if visual:
            drawData(b, ['green' if x == b[j] else 'blue' for x in range(len(data))])

        sleep(speed)
        c[data[j]] -= 1
