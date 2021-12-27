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
root.geometry('500x300')
root.resizable(False, False)
root.title('Radio Button Demo')

labelRows = ttk.Label(text="Number of Rows")
labelRows.pack()
sp1 = Spinbox(root, from_= 3, to = 50) 
sp1.pack()

labelCols = ttk.Label(text="Number of Cols")
labelCols.pack()
sp2 = Spinbox(root, from_= 3, to = 50) 
sp2.pack()


selected_size = tk.StringVar()
sizes = (('1X', 'S'),
         ('2X', 'M'),
         ('4X', 'XXL'))

# label
label = ttk.Label(text="Speed")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)




# button
button = ttk.Button(
    root,
    text="Draw Maze")
    



button.pack()




root.mainloop()
root.mainloop()





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

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Maze Generator")
win = pygame.display.set_mode((Width, Height))
win.fill(DARKBLACK)
pygame.display.update()
Fps = 60
clock = pygame.time.Clock()

a = int(sp1.get())
b = int(sp2.get())



cell_width = 40
x = 0
y = 0

#question = int (input())



grid = [] 
stack_list = []
closed_list = []

path = {}
time.sleep(1)
def build_grid(x, y, cell_width=cell_width):
    for n in range(a):
        x = 40
        y = y + 40
        for m in range(b):
            pygame.draw.line(win, GREY, [x + cell_width, y], [x + cell_width, y + cell_width], 2) # East wall
            pygame.draw.line(win, GREY, [x , y], [x, y + cell_width], 2) # West wall
            pygame.draw.line(win, GREY, [x, y], [x + cell_width, y], 2) # North wall
            pygame.draw.line(win, GREY, [x, y + cell_width], [x + cell_width, y + cell_width], 2) # South wall

            grid.append((x,y))
            x = x + 40
            pygame.display.update()

def Knockdown_East_Wall(x, y):
    pygame.draw.rect(win, GOLD, (x + 1, y + 1, 79, 39), 0)
    pygame.display.update()
def Knockdown_West_Wall(x, y):
    pygame.draw.rect(win, GOLD, (x - cell_width  + 1, y + 1, 79, 39), 0)
    pygame.display.update()
   
def Knockdown_North_Wall(x, y):
    pygame.draw.rect(win, GOLD, (x + 1, y - cell_width + 1, 39, 79), 0)   
    pygame.display.update()
   
def Knockdown_South_Wall(x, y):
    pygame.draw.rect(win, GOLD, (x + 1, y + 1, 39, 79), 0)
    pygame.display.update()

def Single_Cell(x, y):
    pygame.draw.rect(win, BLUE, (x + 1, y + 1, 38, 38), 0)
    pygame.display.update()

def backtracking_cell(x, y):
    pygame.draw.rect(win, GOLD, (x + 1, y+1, 38, 38), 0)
    pygame.display.update()

def Path_tracker(x, y):
    pygame.draw.rect(win, RED, (x + 8, y + 8, 15, 15),0)
    pygame.display.update()
    
def Path_tracker2(x, y):
    pygame.draw.rect(win, BLUE, (x + 8, y + 8, 15, 15),0)
    pygame.display.update()

def Maze(x, y):
    Single_Cell(x, y)
    stack_list.append((x,y))
    closed_list.append((x,y))
    

    while len(stack_list) > 0:
        time.sleep(0.01)
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
            time.sleep(0.01)
            backtracking_cell(x, y)

def path_tracer(x, y):
    Path_tracker(x,y)
    while (x, y) != (40, 40):
        x, y = path[x, y]
        Path_tracker2(x,y)
        time.sleep(0.01)
    Path_tracker(x,y)

x, y = 40, 40
build_grid(40, 0, 40)
Maze(x, y)
path_tracer(random.randrange(1,b-1)*40, (a)*40)

RUN = True
while RUN:
    clock.tick(Fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False