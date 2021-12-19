

#  Friendly Program for some Sorting Algorithms Visualization

#  Written by Mhmd Ali
#  Discord: Andr0x#8929
#  Github: https://github.com/MhmdShd




from time import perf_counter_ns
from tkinter import *
from tkinter import ttk
import random


from Alogs import *

file = open('Simulationn-algo.txt','w')  # open/create Simulation file to write data


root = Tk()   # Application initialization


root.title('sorting')   # Application Name


root.maxsize(1800,1150)    # Application dimention


root.config(bg = 'black')   # Applicatino Background


data = []  # main array


size = 0  # size of the array for simulation



# Drawing Function for visualisation

def drawData(data,color):

    # canvas settings
    canvas.delete('all')
    c_height = 830
    c_width = 1800

    # var width
    x_width = c_width / (len(data)+1)

    for i, height in enumerate(data):

        # left point of rectangle
        x0 = i * x_width
        y0 = c_height - height

        # right point of rectangle
        x1 = (i + 1) * x_width
        y1 = c_height

        # draws rectangle
        canvas.create_rectangle(x0,y0,x1,y1,fill = color[i])

    #update screen
    root.update()


# Generate random Array values ( rectangle height )
def Generate():
    global data

    # Getting values from user input
    minval = int(MinEntry.get())
    maxval = int(MaxEntry.get())
    size = int(sizeEntry.get())


    # settings some conditions for the values
    if minval > maxval : minval,maxval=maxval,minval
    if minval<0:minval=0
    if maxval>830:maxval=830
    if size < 3 : size = 3


    data = [] # emptying data array

    # generating new random data
    for x in range(size):
        data.append((random.randrange(minval,maxval+1)))

    # drawing the data
    drawData(data,['red' for x in range(len(data))])



# simulation functions
def simulate_quick():
    end = 0
    global data

    # cloning data array
    Data = data

    # calling function 500 times for average run time
    for i in range(500):
        start = perf_counter_ns()
        quick_sort(Data, 0, size - 1, drawData, 0)
        end += (perf_counter_ns() - start)/(10**6)

    # writing data to file
    file.write(f'\n     Quick Sort : {end/500} ms')

    # writing data to terminal
    print(f'Quick Sort for n = {size} DONE!! {end/500} ms')

# same comments for the rest of these simulation functions
def simulate_bubble():
    end = 0
    global data
    Data = data
    for i in range(500):
        start = perf_counter_ns()
        bubble_sort(Data,drawData,0)
        end += (perf_counter_ns() - start)/(10**6)
    file.write(f'\n     Bubble Sort : {end/500} ms')
    print(f'Bubble Sort for n = {size} DONE!! {end/500} ms')
def simulate_insertion():
    end = 0
    global data
    Data = data
    for i in range(500):
        start = perf_counter_ns()
        insertion_sort(Data,drawData,0)
        end += (perf_counter_ns() - start)/(10**6)
    file.write(f'\n     Insertion Sort : {end/500} ms')
    print(f'Insertion Sort for n = {size} DONE!! {end/500} ms')
def simulate_selection():
    end = 0
    global data
    Data = data
    for i in range(500):
        start = perf_counter_ns()
        selection_sort(Data,drawData,0)
        end += (perf_counter_ns() - start)/(10**6)
    file.write(f'\n     Selection Sort : {end/500} ms')
    print(f'Selection Sort for n = {size} DONE!! {end/500} ms')
def simulate_merge():
    end = 0
    global data
    Data = data
    for i in range(500):
        start = perf_counter_ns()
        merge_sort(Data,0,size-1,drawData,0)
        end += (perf_counter_ns() - start)/(10**6)
    file.write(f'\n     Merge Sort : {end/500} ms')
    print(f'Merge Sort for n = {size} DONE!! {end/500} ms')
def simulate_heap():
    end = 0
    global data
    Data = data
    for i in range(500):
        start = perf_counter_ns()
        heap_sort(Data,drawData,0)
        end += (perf_counter_ns() - start)/(10**6)
    file.write(f'\n     Heap Sort : {end/500} ms')
    print(f'Heap Sort for n = {size} DONE!! {end/500} ms')
def simulate_counting():
    end = 0
    b=[0]*size
    max = 0
    global data
    Data = data
    for i in range(len(Data)):
        if max < Data[i]: max = Data[i]
    for i in range(500):
        start = perf_counter_ns()
        counting_sort(Data,b,max,drawData,0)
        end += (perf_counter_ns() - start) / (10 ** 6)
    file.write(f'\n     Counting Sort : {end / 500} ms')
    print(f'Counting Sort for n = {size} DONE!! {end/500} ms')



# simulation function
def Simulate():
    global size
    size = 50

    # setting data for simulation
    MinEntry.delete(0,'end')
    MinEntry.insert(0,'1')
    MaxEntry.delete(0,'end')
    MaxEntry.insert(0,'830')
    speedScale.set(0)
    visual.set(0)

    # simulating from size = 50 to size = 500 (increments by 10)
    while size <= 500:

        # setting new size and generating new data
        sizeEntry.delete(0,'end')
        sizeEntry.insert(0,size)
        Generate()

        # writing data to file for organizing
        file.write(f'\nSize = {size} : ')

        # calling simulation functions
        simulate_merge()
        simulate_counting()
        simulate_quick()
        simulate_heap()
        simulate_bubble()
        simulate_selection()
        simulate_insertion()

        size += 10



# calling algorithm functions
def startAlgorithm():
    global data

    # if user didn't generate values yet
    if not data:
        return

    # quick sort
    if (algMenu.get() == 'Quick Sort'):
        if visual.get() == 1:
            quick_sort(data,0,len(data)-1,drawData,speedScale.get(),True)
        else:
            quick_sort(data,0,len(data)-1,drawData,speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # bubble Sort
    elif algMenu.get() == 'Bubble Sort':
        if visual.get() == 1:
            bubble_sort(data, drawData, speedScale.get(),True)
        else:
            bubble_sort(data, drawData, speedScale.get())
        # coloring all elemts green when sorting is complete
        drawData(data, ['green' for x in range(len(data))])

    # Insertion Sort
    elif algMenu.get() == 'Insertion Sort':
        if visual.get() == 1:
            insertion_sort(data,drawData,speedScale.get(),True)
        else:
            insertion_sort(data,drawData,speedScale.get())
        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Selection Sort
    elif algMenu.get() == 'Selection Sort':
        if visual.get() == True:
            selection_sort(data,drawData,speedScale.get(),True)
        else:
            selection_sort(data,drawData,speedScale.get())
        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Merge Sort
    elif algMenu.get() == 'Merge Sort':
        if visual.get()==True:
            merge_sort(data,0,len(data)-1,drawData,speedScale.get(),True)
        else:
            merge_sort(data,0,len(data)-1,drawData,speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Heap Sort
    elif algMenu.get() == 'Heap Sort':
        if visual.get() == True:
            heap_sort(data,drawData,speedScale.get(),True)
        else:
            heap_sort(data,drawData,speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(data, ['green' for x in range(len(data))])

    # Counting Sort
    elif algMenu.get() == 'Counting Sort':
        b = [0]*len(data)

        max = 0
        for i in range(len(data)):
            if max < data[i]:max = data[i]
        if visual.get() == True:
            counting_sort(data,b,max,drawData,speedScale.get(),True)
        else:
            counting_sort(data,b,max,drawData,speedScale.get())

        # coloring all elements green when sorting is finished
        drawData(b,['green' for x in range(len(data))])



# Settings up UI Size

UI_frame = Frame(root,width=1800,height = 300,bg ='grey')
UI_frame.grid(row = 0,column=0,padx = 10, pady = 5)
canvas = Canvas(root, width=1800,height = 830,bg = 'white')
canvas.grid(row = 1,column=0,pady = 5)


# row[0]

# Select Algorithm:
Label(UI_frame,text='Alogorithm: ', bg = "grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu = ttk.Combobox(UI_frame, values = ['Bubble Sort','Heap Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Counting Sort','Merge Sort'])
algMenu.grid(row=0,column=1,padx=5,pady=5)
algMenu.current(0)

# speed scale
speedScale = Scale(UI_frame,from_=0,to=5,length=100,digits=2,resolution=0.2,orient = HORIZONTAL,label = 'Select Delay [s]')
speedScale.grid(row = 0,column=2,padx=5,pady=5)

# visual box ( show step by step )
visual = Scale(UI_frame,from_=0,to=1,length=100,digits=2,resolution=1,orient = HORIZONTAL,label = 'Visualise? [0/1]')
visual.grid(row = 0,column=3,padx=5,pady=5)

# start button
Button(UI_frame,text='Start',command=startAlgorithm,bg='green').grid(row=0,column=4,padx=5,pady=5)


Label(UI_frame,text='when clicked, check terminal:',bg = 'grey').grid(row=0,column=5,pady=5,padx=5)


# simulation button (don't click, it will take alot of time to finish)
Button(UI_frame,text='Simulate',command=Simulate,bg='red').grid(row=0,column=6,padx=5,pady=5)


# row[1]

# select size

Label(UI_frame,text='Size: ', bg = "grey").grid(row=1,column=0,padx=5,pady=5,sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1,column=1,padx=5,pady=5,sticky = W)


# minimume value

Label(UI_frame,text='Min Value: ', bg = "grey").grid(row=1,column=2,padx=5,pady=5,sticky=W)
MinEntry = Entry(UI_frame)
MinEntry.grid(row=1,column=3,padx=5,pady=5,sticky = W)


# max Value

Label(UI_frame,text='Max Value: ', bg = "grey").grid(row=1,column=4,padx=5,pady=5,sticky=W)
MaxEntry = Entry(UI_frame)
MaxEntry.grid(row=1,column=5,padx=5,pady=5,sticky = W)


# generate Vutton
Button(UI_frame,text='Generate',command=Generate,bg='yellow').grid(row=1,column=6,padx=5,pady=5)



root.mainloop()