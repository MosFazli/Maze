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
root.geometry('400x700')
root.resizable(False, False)
root.title('Radio Button Demo')


########################################################

sp1 = IntVar()
it1 = sp1.get()
sp2 = IntVar()
it2 = sp2.get()

labelRows = ttk.Label(text="Number of Rows")
labelRows.pack()
sp1 = Spinbox(root, from_= 10, to = 38)
sp1.pack()

labelCols = ttk.Label(text="Number of Cols")
labelCols.pack()
sp2 = Spinbox(root, from_= 10, to = 73)
sp2.pack()

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


########################################################


def get_values():
    global x
    global y
    global sped
    global backTrack
    global solving
    global cellSize
    x = (sp1.get())
    y = (sp2.get())
    sped = speedRadio.get()
    backTrack = showBacktracking.get()
    solving = solveMaze.get()
    cellSize = mazeSize.get()
    print("Num of Rows: " + x)
    print("Num of Cols: " + y)
    print("Speed of geme: " + str(sped))
    print("Backtracking Avaliable: " + str(backTrack))
    print("Solve Maze: " + str(solving))
    print("Maze size: " + str(cellSize))
    root.destroy()

# button
button = ttk.Button(
    root,
    text="Draw Maze",command = get_values)


button.pack()

root.mainloop()




start = time.time()
#BLACK = (49, 78, 82)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 187, 204)
GREY = (49, 78, 82)
DARKBLACK = (27, 26, 23)

GOLD = (235, 168, 58)
RED = (187, 55, 26)
WHITE = (255, 248, 217)

Width, Height = 1500, 800

back = backTrack
solver = solving

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Maze Generator")
win = pygame.display.set_mode((Width, Height))
win.fill(DARKBLACK)
pygame.display.update()
frames = 50
clock = pygame.time.Clock()

a = int(x)
b = int(y)


cell_width = cellSize
x = 0
y = 0

speed = sped

#question = int (input())



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
            pygame.draw.line(win, GREY, [x + cell_width, y], [x + cell_width, y + cell_width], 2) # East wall
            pygame.draw.line(win, GREY, [x , y], [x, y + cell_width], 2) # West wall
            pygame.draw.line(win, GREY, [x, y], [x + cell_width, y], 2) # North wall
            pygame.draw.line(win, GREY, [x, y + cell_width], [x + cell_width, y + cell_width], 2) # South wall

            grid.append((x,y))
            x = x + cell_width
            pygame.display.update()

def Knockdown_East_Wall(x, y):
    pygame.draw.rect(win, WHITE, (x + 1, y + 1, (2*cell_width)-1, cell_width-1), 0)
    pygame.display.update()
def Knockdown_West_Wall(x, y):
    pygame.draw.rect(win, WHITE, (x - cell_width  + 1, y + 1, (2*cell_width)-1, cell_width-1), 0)
    pygame.display.update()
   
def Knockdown_North_Wall(x, y):
    pygame.draw.rect(win, WHITE, (x + 1, y - cell_width + 1, cell_width-1, (2*cell_width)-1,), 0)
    pygame.display.update()
   
def Knockdown_South_Wall(x, y):
    pygame.draw.rect(win, WHITE, (x + 1, y + 1, cell_width-1, (2*cell_width)-1), 0)
    pygame.display.update()

def Single_Cell(x, y):
    pygame.draw.rect(win, BLUE, (x + 1, y + 1, cell_width-2, cell_width-2), 0)
    pygame.display.update()

if back == 0:
    def backtracking_cell(x, y):
        pygame.draw.rect(win, WHITE, (x + 1, y+1, cell_width-2, cell_width-2), 0)
        pygame.display.update()

if back == 1:
    def backtracking_cell(x, y):
        pygame.draw.rect(win, GOLD, (x + 1, y+1, cell_width-2, cell_width-2), 0)
        pygame.display.update()


def Path_tracker(x, y):
    pygame.draw.rect(win, RED, (x + 8, y + 8, cell_width/2.5, cell_width/2.5),0)
    pygame.display.update()
    
def Path_tracker2(x, y):
    pygame.draw.rect(win, BLUE, (x + 8, y + 8, cell_width/2.5, cell_width/2.5),0)
    pygame.display.update()

def Maze(x, y):
    Single_Cell(x, y)
    stack_list.append((x,y))
    closed_list.append((x,y))
    

    while len(stack_list) > 0:
        time.sleep(speed)
        cell = []

        if(x + cell_width, y) not in closed_list and (x + cell_width, y) in grid:
            cell.append("East")

        if (x - cell_width, y) not in closed_list and (x - cell_width, y) in grid:
            cell.append("West")

        if (x , y + cell_width) not in closed_list and (x , y + cell_width) in grid:
            cell.append("South")

        if (x, y - cell_width) not in closed_list and (x , y - cell_width) in grid:
            cell.append("North") 

        if len(cell) > 0:
            current_cell = (random.choice(cell))

            if current_cell == "East":
                Knockdown_East_Wall(x,y)
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
                path[(x , y - cell_width)] = x, y
                y = y - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "South":
                Knockdown_South_Wall(x, y)
                path[(x , y + cell_width)] = x, y
                y = y + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

        else:
            x, y = stack_list.pop()
            Single_Cell(x, y)
            time.sleep(speed)
            backtracking_cell(x, y)

def path_tracer(x, y):
    Path_tracker(x,y)
    if solver == 1:
        while (x, y) != (cell_width, cell_width):
            x, y = path[x, y]
            Path_tracker2(x,y)
            time.sleep(speed)
    Path_tracker(x,y)

x, y = cell_width, cell_width
build_grid(cell_width, 0, cell_width)
Maze(x, y)

path_tracer(random.randrange(1,b-1)*cell_width, (a)*cell_width)

end = time.time()

print('Time: ', end - start)

RUN = True
while RUN:
    clock.tick(frames)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False