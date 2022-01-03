""""
Maze Program
this program developed by Mostafa Fazli, Danial Bayati, Foad Ataei, Ali Toosi
Excess Practice of Artificial Intelligence
3 Jan 2022
"""


import math
from os import remove
import random
import time
from tkinter import simpledialog
import pygame

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

from pygame.event import get

# root window

a = 15
b = 15

root = tk.Tk()
root.geometry('420x980')
root.resizable(False, False)
root.title('Maze Control Menu')

########################################################


sp1 = IntVar()
it1 = sp1.get()
sp2 = IntVar()
it2 = sp2.get()

labelRows = ttk.Label(text="Number of Rows")
# labelRows.pack()
sp1 = Spinbox(root, from_=15, to=38)

labelCols = ttk.Label(text="Number of Cols")
# labelCols.pack()
sp2 = Spinbox(root, from_=20, to=73)

########################################################

speedRadio = DoubleVar()
sizes = [('1X', 0.2),
         ('2X', 0.1),
         ('3X', 0.05),
         ('4X', 0.025),
         ('5X', 0.01),
         ('Without pause', 0)
         ]

showBacktracking = IntVar()
backs = [('No', 0),
         ('Yes', 1),
         ]
solveMaze = IntVar()
solves = [('No', 0),
          ('Yes', 1),
          ]

mazeSize = IntVar()
mazeSizes = [('Small', 20),
             ('Medium', 40),
             ('Large', 60),
             ]

# label
label = ttk.Label(text="Speed")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=speedRadio
    )
    r.pack(fill='x', padx=5, pady=5)

label2 = ttk.Label(text="Do you want to see backtracking ?")
label2.pack(fill='x', padx=5, pady=5)
# radio buttons
for size in backs:
    r2 = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=showBacktracking
    )
    r2.pack(fill='x', padx=5, pady=5)

label3 = ttk.Label(text="Do you want to Solve it ?")
label3.pack(fill='x', padx=5, pady=5)
# radio buttons
for size in solves:
    r3 = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=solveMaze
    )
    r3.pack(fill='x', padx=5, pady=5)

label4 = ttk.Label(text="Size of cells:")
label4.pack(fill='x', padx=5, pady=5)
# radio buttons
for size in mazeSizes:
    r4 = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=mazeSize
    )
    r4.pack(fill='x', padx=5, pady=5)

########################################################

is_on = True

# Create Label
my_label = Label(root,
                 text="Dark Theme",
                 fg="grey",
                 font=("Helvetica", 10))

my_label.pack()


# Define our switch function
def switch():
    global is_on

    # Determine is on or off
    if is_on:
        on_button.config(image=off)
        my_label.config(text="Dark Mode Disabled!",
                        fg="grey")
        is_on = False
    else:
        on_button.config(image=on)
        my_label.config(text="Dark Mode Enabled!", fg="green")
        is_on = True


# Define Our Images
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

# Create A Button
on_button = Button(root, image=on, bd=0,
                   command=switch)
on_button.pack(pady=5)

########################################################

is_on2 = True

# Create Label
my_label2 = Label(root,
                  text="Cpmplicated Mode",
                  fg="grey",
                  font=("Helvetica", 10))

my_label2.pack()


# Define our switch function
def switch2():
    global is_on2

    # Determine is on or off
    if is_on2:
        on_button2.config(image=off)
        my_label2.config(text="not Cpmplicated!",
                         fg="grey")
        is_on2 = False
    else:
        on_button2.config(image=on)
        my_label2.config(text="Cpmplicated!", fg="green")
        is_on2 = True


# Define Our Images
on2 = PhotoImage(file="on.png")
off2 = PhotoImage(file="off.png")

# Create A Button
on_button2 = Button(root, image=on2, bd=0,
                    command=switch2)
on_button2.pack(pady=5)

########################################################


is_on3 = True

# Create Label
my_label3 = Label(root,
                  text="Scrren Mode",
                  fg="grey",
                  font=("Helvetica", 10))

my_label3.pack()


# Define our switch function
def switch3():
    global is_on3

    # Determine is on or off
    if is_on3:
        on_button3.config(image=off)
        my_label3.config(text="Not Fullscreen",
                         fg="grey")
        is_on3 = False
    else:
        on_button3.config(image=on)
        my_label3.config(text="Fullscreen", fg="green")
        is_on3 = True


# Define Our Images
on3 = PhotoImage(file="on.png")
off3 = PhotoImage(file="off.png")

# Create A Button
on_button3 = Button(root, image=on3, bd=0,
                    command=switch3)
on_button3.pack(pady=5)

########################################################

cellsNum = IntVar()
num = cellsNum.get()

labelNumofCells = ttk.Label(text="Number of Cells")
# labelRows.pack()
cellsNum = Spinbox(root, from_=15, to=38)


########################################################

is_on4 = True

# Create Label
my_label4 = Label(root, text="Draw with Cols and Rows", fg="grey", font=("Helvetica", 10))


# Define our switch function
def switch4():
    global is_on4

    # Determine is on or off
    if is_on4:
        on_button4.config(image=off)
        my_label4.config(text="with Number of Cells",
                         fg="grey")
        is_on4 = False
        labelRows.pack_forget()
        sp1.pack_forget()
        labelCols.pack_forget()
        sp2.pack_forget()
        labelNumofCells.pack()
        cellsNum.pack()
    else:
        on_button4.config(image=on)
        my_label4.config(text="Cols and Rows", fg="green")
        is_on4 = True
        labelNumofCells.pack_forget()
        cellsNum.pack_forget()
        labelRows.pack()
        sp1.pack()
        labelCols.pack()
        sp2.pack()
        root.update()


# Define Our Images
on4 = PhotoImage(file="on.png")
off4 = PhotoImage(file="off.png")

# Create A Button
my_label4.pack()
on_button4 = Button(root, image=on4, bd=0, command=switch4)
on_button4.pack(pady=5)

labelRows.pack()
sp1.pack()
labelCols.pack()
sp2.pack()


########################################################


def get_values():
    global x
    global y
    global sped
    global backTrack
    global solving
    global cellSize
    if is_on4 == True:
        x = (sp1.get())
        y = (sp2.get())
    else:
        flag = False
        z = int(cellsNum.get())
        n = int(math.sqrt(z))
        for i in range (n,-1,-1):
            for j in range (n,z,1):
                if (i * j) == z:
                    x = i
                    y = j
                    flag = True
                    break
            if flag == True:
                break

    sped = speedRadio.get()
    backTrack = showBacktracking.get()
    solving = solveMaze.get()
    cellSize = mazeSize.get()
    print("Num of Rows: " + str(x))
    print("Num of Cols: " + str(y))
    print("Speed of geme: " + str(sped))
    print("Backtracking Avaliable: " + str(backTrack))
    print("Solve Maze: " + str(solving))
    print("Maze size: " + str(cellSize))
    root.destroy()


# button
button = ttk.Button(
    root,
    text="Draw Maze", command=get_values)

button.pack()

root.mainloop()

start = time.time()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 187, 204)

lineColor = (216, 146, 22)
GREY = (55, 64, 69)
BRIGHTGOLD = (225, 216, 159)

background = (163, 177, 138)
DARKBLACK = (50, 50, 50)
BRIGHTGREEN = (218, 215, 205)

cellColor = (255, 248, 217)
BLACK = (82, 82, 82)
WHITE = (255, 248, 217)

backtrackingColor = (50, 59, 64)
backWHITE = (240, 233, 202)
backBLACK = (97, 97, 97)

darkMode = is_on

if is_on == False:
    darkMode = False
else:
    darkMode = True

if darkMode == False:
    background = BRIGHTGREEN
    cellColor = WHITE
    lineColor = GREY
    backtrackingColor = backWHITE

else:
    background = DARKBLACK
    cellColor = BLACK
    lineColor = BRIGHTGOLD
    backtrackingColor = backBLACK

RED = (187, 55, 26)

Width, Height = 1500, 800

back = backTrack
solver = solving

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Maze Generator")
win = pygame.display.set_mode((Width, Height))
win.fill(background)
if is_on3 == True:
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.update()
frames = 50
clock = pygame.time.Clock()

a = int(x)
b = int(y)

cell_width = cellSize
x = 0
y = 0

speed = sped

# question = int (input())


grid = []
stack_list = []
closed_list = []

path = {}
time.sleep(1)


def build_grid(x, y, cell_width=cell_width):
    for n in range(a):
        x = cell_width
        y = y + cell_width
        for m in range(b):
            pygame.draw.line(win, lineColor, [x + cell_width, y], [x + cell_width, y + cell_width], 2)  # East wall
            pygame.draw.line(win, lineColor, [x, y], [x, y + cell_width], 2)  # West wall
            pygame.draw.line(win, lineColor, [x, y], [x + cell_width, y], 2)  # North wall
            pygame.draw.line(win, lineColor, [x, y + cell_width], [x + cell_width, y + cell_width], 2)  # South wall

            grid.append((x, y))
            x = x + cell_width
            pygame.display.update()


def Knockdown_East_Wall(x, y):
    pygame.draw.rect(win, cellColor, (x + 1, y + 1, (2 * cell_width) - 1, cell_width - 1), 0)
    pygame.display.update()


def Knockdown_West_Wall(x, y):
    pygame.draw.rect(win, cellColor, (x - cell_width + 1, y + 1, (2 * cell_width) - 1, cell_width - 1), 0)
    pygame.display.update()


def Knockdown_North_Wall(x, y):
    pygame.draw.rect(win, cellColor, (x + 1, y - cell_width + 1, cell_width - 1, (2 * cell_width) - 1,), 0)
    pygame.display.update()


def Knockdown_South_Wall(x, y):
    pygame.draw.rect(win, cellColor, (x + 1, y + 1, cell_width - 1, (2 * cell_width) - 1), 0)
    pygame.display.update()


def Single_Cell(x, y):
    pygame.draw.rect(win, BLUE, (x + 1, y + 1, cell_width - 2, cell_width - 2), 0)
    pygame.display.update()


if back == 0:
    def backtracking_cell(x, y):
        pygame.draw.rect(win, cellColor, (x + 1, y + 1, cell_width - 2, cell_width - 2), 0)
        pygame.display.update()

if back == 1:
    def backtracking_cell(x, y):
        pygame.draw.rect(win, backtrackingColor, (x + 1, y + 1, cell_width - 2, cell_width - 2), 0)
        pygame.display.update()


def Path_tracker(x, y):
    pygame.draw.rect(win, RED, (x + 8, y + 8, cell_width / 2.5, cell_width / 2.5), 0)
    pygame.display.update()


def Path_tracker2(x, y):
    pygame.draw.rect(win, BLUE, (x + 8, y + 8, cell_width / 2.5, cell_width / 2.5), 0)
    pygame.display.update()


def Maze(x, y):
    Single_Cell(x, y)
    stack_list.append((x, y))
    closed_list.append((x, y))

    while len(stack_list) > 0:
        time.sleep(speed)
        cell = []

        if (x + cell_width, y) not in closed_list and (x + cell_width, y) in grid:
            cell.append("East")

        if (x - cell_width, y) not in closed_list and (x - cell_width, y) in grid:
            cell.append("West")

        if (x, y + cell_width) not in closed_list and (x, y + cell_width) in grid:
            cell.append("South")

        if (x, y - cell_width) not in closed_list and (x, y - cell_width) in grid:
            cell.append("North")

        if len(cell) > 0:
            current_cell = (random.choice(cell))

            if current_cell == "East":
                Knockdown_East_Wall(x, y)
                path[(x + cell_width, y)] = x, y
                x = x + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "West":
                Knockdown_West_Wall(x, y)
                path[(x - cell_width, y)] = x, y
                x = x - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "North":
                Knockdown_North_Wall(x, y)
                path[(x, y - cell_width)] = x, y
                y = y - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "South":
                Knockdown_South_Wall(x, y)
                path[(x, y + cell_width)] = x, y
                y = y + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

        else:
            x, y = stack_list.pop()
            Single_Cell(x, y)
            time.sleep(speed)
            backtracking_cell(x, y)


def path_tracer(x, y):
    Path_tracker(x, y)
    if solver == 1:
        while (x, y) != (cell_width, cell_width):
            x, y = path[x, y]
            Path_tracker2(x, y)
            time.sleep(speed)
    Path_tracker(x, y)


x, y = cell_width, cell_width
build_grid(cell_width, 0, cell_width)
Maze(x, y)

if is_on2 == False:
    path_tracer(random.randrange(1, b - 1) * cell_width, (a) * cell_width)
else:
    path_tracer(random.randrange(int((b - 1) / 2) +1, b - 1) * cell_width, (a) * cell_width)

end = time.time()

print('Time: ', end - start)

RUN = True
while RUN:
    clock.tick(frames)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False