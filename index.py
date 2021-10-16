from tkinter import *
from math import floor

menu = Tk()


def click(e):
    print(e)


class Grid():
    def __init__(self, window: Tk, cell_size: int) -> None:
        self.cells = []
        self.cell_size = cell_size
        self.window = window
        self.canvas = Canvas(window, height=cell_size*3, width=cell_size*3)
        self.canvas.pack()
        for i in range(9):
            self.cells.append(Cell(i, self.canvas))
        for cell in self.cells:
            self.canvas.create_rectangle(
                cell.x*cell_size+2, cell.y*cell_size+2, cell.x*cell_size+cell_size-1, cell.y*cell_size+cell_size-1)
            cell.draw()

    def click_event(self, e: Event):
        x = floor(e.x / self.cell_size)
        y = floor(e.y / self.cell_size)
        self.cells[y*3+x].click_event()


class Cell():
    def __init__(self, index: int, canvas: Canvas) -> None:
        self.value = ""
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.canvas = canvas

    def draw(self) -> None:
        self.canvas.create_oval(self.x*50+5, self.y*50+5,
                                self.x*50+45, self.y*50+45)

    def click_event(self):
        print(self.index)


grid = Grid(menu, 50)
menu.bind("<Button-1>", grid.click_event)
menu.mainloop()
