from tkinter import *
from math import floor

menu = Tk()

def test(e):
    print(e)

class Cell():
    def __init__(self, index:int, window: Tk) -> None:
        self.value = ""
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.window = window
        self.label = Label(window, text=" ")
        self.label.grid(row=self.y, column=self.x)
        self.label.bind("<Button-1>", test)

class Grid():
    def __init__(self, window: Tk) -> None:
        self.cells = []
        self.window = window
        for i in range(9):
            self.cells.append(Cell(i, window))

Grid(menu)
menu.bind("<Button-1>", test)
menu.mainloop()
