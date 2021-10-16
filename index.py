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
        self.ended = False

        for i in range(9):
            self.cells.append(Cell(i, self))
        for cell in self.cells:
            self.canvas.create_rectangle(
                cell.x*cell_size+2, cell.y*cell_size+2, cell.x*cell_size+cell_size-1, cell.y*cell_size+cell_size-1)
            cell.draw()

    def click_event(self, e: Event):
        x = floor(e.x / self.cell_size)
        y = floor(e.y / self.cell_size)
        index = y*3+x
        if(not (index < 0 or index > 8 or x < 0 or x > 2 or y < 0 or y > 2)):
            self.cells[index].click_event()
            self.checkWin()

    def checkWin(self):
        for i in range(3):
            state = self.cells[i*3].value
            for j in range(3):
                if(state != self.cells[i*3+j].value):
                    state = ""
            if(state != ""):
                self.ended = True
                self.labelText.set("{} won".format(state))

        for i in range(3):
            state = self.cells[i].value
            for j in range(3):
                if(state != self.cells[i+j*3].value):
                    state = ""
            if(state != ""):
                self.ended = True
                self.labelText.set("{} won".format(state))

        state = self.cells[0].value
        for i in (4, 8):
            if(state != self.cells[i].value):
                state = ""
        if(state != ""):
            self.ended = True
            self.labelText.set("{} won".format(state))

        state = self.cells[2].value
        for i in (4, 6):
            if(state != self.cells[i].value):
                state = ""
        if(state != ""):
            self.ended = True
            self.labelText.set("{} won".format(state))


class Cell():
    def __init__(self, index: int, grid: Grid) -> None:
        self.value: str = ""
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.canvas: Canvas = grid.canvas
        self.size: int = grid.cell_size
        self.grid: Grid = grid

    def draw(self):
        if(self.value == "o"):
            self.canvas.create_oval(self.x*self.size+self.size/10, self.y*self.size+self.size/10,
                                    self.x*self.size+self.size/10*9, self.y*self.size+self.size/10*9)
        if(self.value == "x"):
            self.canvas.create_line(self.x*self.size+self.size/10, self.y*self.size+self.size/10,
                                    self.x*self.size+self.size/10*9, self.y*self.size+self.size/10*9)
            self.canvas.create_line(self.x*self.size+self.size/10*9, self.y*self.size+self.size/10,
                                    self.x*self.size+self.size/10, self.y*self.size+self.size/10*9)

    def click_event(self):
        if(self.value == "" and self.grid.ended == False):
            self.value = self.grid.turn
            self.grid.turn = ("x", "o")[self.grid.turn == "x"]
            self.grid.labelText.set("{}'s turn".format(self.grid.turn))
            self.draw()


grid = Grid(window, 100)
window.bind("<Button-1>", grid.click_event)
window.mainloop()
