from tkinter import *
from math import floor

window = Tk()


def click(e):
    print(e)


class Grid():
    def __init__(self, window: Tk, cell_size: int) -> None:
        self.cells = []
        self.cell_size = cell_size
        self.window = window
        self.canvas = Canvas(window, height=cell_size*3, width=cell_size*3)
        self.canvas.pack()
        self.canvas.grid(column=0, row=1)
        self.labelText = StringVar()
        self.labelText.set("x's turn")
        self.label: Label = Label(self.window, textvariable=self.labelText)
        self.label.grid(column=0, row=0)
        self.turn = "x"

        for i in range(9):
            self.cells.append(Cell(i, self))
        for cell in self.cells:
            self.canvas.create_rectangle(
                cell.x*cell_size+2, cell.y*cell_size+2, cell.x*cell_size+cell_size-1, cell.y*cell_size+cell_size-1)
            cell.draw()

    def click_event(self, e: Event):
        x = floor(e.x / self.cell_size)
        y = floor(e.y / self.cell_size)
        self.cells[y*3+x].click_event()


class Cell():
    def __init__(self, index: int, grid: Grid) -> None:
        self.value = ""
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.canvas: Canvas = grid.canvas
        self.size: int = grid.cell_size
        self.grid: Grid = grid

    def draw(self) -> None:
        if(self.value == "o"):
            self.canvas.create_oval(self.x*self.size+self.size/10, self.y*self.size+self.size/10,
                                    self.x*self.size+self.size/10*9, self.y*self.size+self.size/10*9)
        if(self.value == "x"):
            self.canvas.create_line(self.x*self.size+self.size/10, self.y*self.size+self.size/10,
                                    self.x*self.size+self.size/10*9, self.y*self.size+self.size/10*9)
            self.canvas.create_line(self.x*self.size+self.size/10*9, self.y*self.size+self.size/10,
                                    self.x*self.size+self.size/10, self.y*self.size+self.size/10*9)

    def click_event(self):
        if(self.value == ""):
            self.value = self.grid.turn
            self.grid.turn = ("x", "o")[self.grid.turn == "x"]
            self.grid.labelText.set("{}'s turn".format(self.grid.turn))
            self.draw()


grid = Grid(window, 100)
window.bind("<Button-1>", grid.click_event)
window.mainloop()
