#  Friendly Program for some Sorting Algorithms Visualization

#  Written by Mhmd Ali
#  Discord: Andr0x#8929
#  Github: https://github.com/MhmdShd


from time import perf_counter_ns
from tkinter import *
from tkinter import ttk
import random

from Alogs import *

from Graph import Plot

file = None

root = Tk()  # Application initialization

root.title('sorting')  # Application Name

root.maxsize(1800, 1150)  # Application dimention

root.config(bg='black')  # Applicatino Background

data = []  # main array

size = 0  # size of the array for simulation

userFile = None  # file for user

userArray = []  # array for user


# Drawing Function for visualisation

def drawData(data, color):
    # canvas settings
    canvas.delete('all')
    c_height = 700
    c_width = 1800

    # var width
    x_width = c_width / (len(data) + 1)

    for i, height in enumerate(data):
        # left point of rectangle
        x0 = i * x_width
        y0 = c_height - height

        # right point of rectangle
        x1 = (i + 1) * x_width
        y1 = c_height

        # draws rectangle
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    # update screen
    root.update()


# Generate random Array values ( rectangle height )
def Generate(visual=True):
    global data

    # Getting values from user input
    minval = int(MinEntry.get())
    maxval = int(MaxEntry.get())
    size = int(sizeEntry.get())

    # settings some conditions for the values
    if minval > maxval: minval, maxval = maxval, minval
    if minval < 0: minval = 0
    if maxval > 700: maxval = 700
    if size < 3: size = 3

    data = []  # emptying data array

    # generating new random data
    for x in range(size):
        data.append((random.randrange(minval, maxval + 1)))

    # drawing the data

    if visual == True:  # False for Simulation
        drawData(data, ['red' for x in range(len(data))])


# simulation function

def Simulate():
    global size
    size = 50
    global file

    file = open('Simulation-algo.txt', 'w')  # open/create Simulation file to write data
    # setting data for simulation
    MinEntry.delete(0, 'end')
    MinEntry.insert(0, '1')
    MaxEntry.delete(0, 'end')
    MaxEntry.insert(0, '700')
    speedScale.set(0)
    visual.set(0)

    file.write('{\n   "Simulation Details": [')
    # simulating from size = 50 to size = 500 (increments by 10)

    while size <= 500:

        # setting new size and generating new data
        sizeEntry.delete(0, 'end')
        sizeEntry.insert(0, size)

        # writing data to file for organizing
        if size > 50:
            file.write(',')
        file.write('\n      {')
        file.write(f'\n         "Size" : "{size}",')

        # calling simulation functions
        simulate_merge()
        simulate_counting()
        simulate_quick()
        simulate_heap()
        simulate_bubble()
        simulate_selection()
        simulate_insertion()
        file.write('\n      }')
        size += 10

    file.write('\n  ]\n}')
    file.close()
    Plot()


# simulation functions

def simulate_quick():
    # variable for time duration
    end = 0

    # variable for the file to write data on
    global file

    # calling function 500 times for average run time
    for i in range(500):
        # generate new data with no drawing
        Generate(False)

        # calculating average run time for the algorithm
        start = perf_counter_ns()
        quick_sort(data, 0, size - 1, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)

    # writing data to file
    file.write(f'\n         "Quick Sort" : "{end}",')

    # writing data to terminal
    print(f'Quick Sort for n = {size} DONE!! {end} ms')


# same comments for the rest of these simulation functions
def simulate_bubble():
    end = 0
    global file
    for i in range(500):
        Generate(False)
        start = perf_counter_ns()
        bubble_sort(data, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)
    file.write(f'\n         "Bubble Sort" : "{end}",')
    print(f'Bubble Sort for n = {size} DONE!! {end} ms')


def simulate_insertion():
    end = 0
    global file
    for i in range(500):
        Generate(False)
        start = perf_counter_ns()
        insertion_sort(data, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)
    file.write(f'\n         "Insertion Sort" : "{end}"')
    print(f'Insertion Sort for n = {size} DONE!! {end} ms')


def simulate_selection():
    end = 0
    global file
    for i in range(500):
        Generate(False)
        start = perf_counter_ns()
        selection_sort(data, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)
    file.write(f'\n         "Selection Sort" : "{end}",')
    print(f'Selection Sort for n = {size} DONE!! {end} ms')


def simulate_merge():
    end = 0
    global file
    for i in range(500):
        Generate(False)
        start = perf_counter_ns()
        merge_sort(data, 0, size - 1, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)
    file.write(f'\n         "Merge Sort" : "{end}",')
    print(f'Merge Sort for n = {size} DONE!! {end} ms')


def simulate_heap():
    end = 0
    global file
    for i in range(500):
        Generate(False)
        start = perf_counter_ns()
        heap_sort(data, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)
    file.write(f'\n         "Heap Sort" : "{end}",')
    print(f'Heap Sort for n = {size} DONE!! {end} ms')


def simulate_counting():
    end = 0
    global file
    b = [0] * size
    max = 0
    for i in range(500):
        Generate(False)

        # getting max value in the array
        for i in range(len(data)):
            if max < data[i]: max = data[i]

        start = perf_counter_ns()
        counting_sort(data, b, max, drawData, 0)
        end += (perf_counter_ns() - start) / (500000000)

    file.write(f'\n         "Counting Sort" : "{end}",')
    print(f'Counting Sort for n = {size} DONE!! {end} ms')


# calling algorithm functions
def startAlgorithm():
    global data

    # if user didn't generate values yet
    if not data:
        return

    # quick sort
    if (algMenu.get() == 'Quick Sort'):
        if visual.get() == 1:
            quick_sort(data, 0, len(data) - 1, drawData, speedScale.get(), True)
        else:
            quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # bubble Sort
    elif algMenu.get() == 'Bubble Sort':
        if visual.get() == 1:
            bubble_sort(data, drawData, speedScale.get(), True)
        else:
            bubble_sort(data, drawData, speedScale.get())

        # coloring all elements green when sorting is complete
        drawData(data, ['green' for x in range(len(data))])

    # Insertion Sort
    elif algMenu.get() == 'Insertion Sort':

        if visual.get() == 1:
            insertion_sort(data, drawData, speedScale.get(), True)
        else:
            insertion_sort(data, drawData, speedScale.get())
        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Selection Sort
    elif algMenu.get() == 'Selection Sort':
        if visual.get() == 1:
            selection_sort(data, drawData, speedScale.get(), True)
        else:
            selection_sort(data, drawData, speedScale.get())
        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Merge Sort
    elif algMenu.get() == 'Merge Sort':
        if visual.get() == 1:
            merge_sort(data, 0, len(data) - 1, drawData, speedScale.get(), True)
        else:
            merge_sort(data, 0, len(data) - 1, drawData, speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Heap Sort
    elif algMenu.get() == 'Heap Sort':
        if visual.get() == 1:
            heap_sort(data, drawData, speedScale.get(), True)
        else:
            heap_sort(data, drawData, speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Counting Sort
    elif algMenu.get() == 'Counting Sort':
        b = [0] * len(data)

        max = 0
        for i in range(len(data)):
            if max < data[i]: max = data[i]
        if visual.get() == 1:
            counting_sort(data, b, max, drawData, speedScale.get(), True)
        else:
            counting_sort(data, b, max, drawData, speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(b, ['green' for x in range(len(data))])


def addToUserArray():
    global userArray

    # adds the value to the array
    userArray.append(int(user_arrayEntry.get()))

    # empty the text box
    user_arrayEntry.delete(0, 'end')

    # Default value = 0
    user_arrayEntry.insert(0, '0')


def openFile():
    global userFile
    global userArray

    # open/create a file to type in the sorted array
    userFile = open('Sorted_array.txt', 'w')

    # visualize the array
    if visual == 1:
        drawData(userArray, ['red' for x in range(len(userArray))])

    b = [0] * len(userArray)

    # max value for the counting sort
    max = 0
    for i in range(len(userArray)):
        if max < userArray[i]: max = userArray[i]

    # calling counting sort
    counting_sort(userArray, b, max, drawData, speedScale.get(), visual.get())

    # drawing the sorted array if the user chose to
    if visual == 1:
        drawData(b, ['green' for x in range(len(userArray))])

    # typing the sorted array inside the opened file
    for i in range(len(userArray)):
        userFile.write(f'{b[i]},')
    userFile.close()


    print('File created "Sorted_array.txt" Contains your array sorted!')


# Settings up UI Size

UI_frame = Frame(root, width=1800, height=450, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=1800, height=700, bg='white')
canvas.grid(row=1, column=0, pady=5)

# row[0]

# Select Algorithm:
Label(UI_frame, text='Alogorithm: ', bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, values=['Bubble Sort', 'Heap Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort',
                                         'Counting Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

# speed scale
speedScale = Scale(UI_frame, from_=0, to=5, length=100, digits=2, resolution=0.2, orient=HORIZONTAL,
                   label='Select Delay [s]')
speedScale.grid(row=0, column=2, padx=5, pady=5)

# visual box ( show step by step )
visual = Scale(UI_frame, from_=0, to=1, length=100, digits=2, resolution=1, orient=HORIZONTAL, label='Visualise? [0/1]')
visual.grid(row=0, column=3, padx=5, pady=5)

# start button
Button(UI_frame, text='Start', command=startAlgorithm, bg='green').grid(row=0, column=4, padx=5, pady=5)

Label(UI_frame, text='when clicked, check terminal:', bg='grey').grid(row=0, column=5, pady=5, padx=5)

# simulation button (don't click, it will take alot of time to finish)
Button(UI_frame, text='Simulate', command=Simulate, bg='red').grid(row=0, column=6, padx=5, pady=5)

# row[1]

# select size

Label(UI_frame, text='Size: ', bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# minimum value

Label(UI_frame, text='Min Value: ', bg="grey").grid(row=1, column=2, padx=5, pady=5, sticky=W)
MinEntry = Entry(UI_frame)
MinEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# max Value

Label(UI_frame, text='Max Value: ', bg="grey").grid(row=1, column=4, padx=5, pady=5, sticky=W)
MaxEntry = Entry(UI_frame)
MaxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

# Generate Button
Button(UI_frame, text='Generate', command=Generate, bg='yellow').grid(row=1, column=6, padx=5, pady=5)

# Lets the user to enter his own array to sort it
Label(UI_frame, text='Sort Your Own Array! ( Check Terminal after sorting )', bg="grey").grid(row=2, column=3, padx=5, pady=5, sticky=W)

# receives value from the user
Label(UI_frame, text='Enter Array: ', bg="grey").grid(row=3, column=0, padx=5, pady=5, sticky=W)
user_arrayEntry = Entry(UI_frame)
user_arrayEntry.insert(0, '0')
user_arrayEntry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

# submit the value and add it to the array
Button(UI_frame, text='Add Value to array', command=addToUserArray, bg='yellow').grid(row=3, column=2, padx=5, pady=5)

# sort the array the user have created
Button(UI_frame, text='Get Sorted Array', command=openFile, bg='green').grid(row=3, column=3, padx=5, pady=5)

root.mainloop()
