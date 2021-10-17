from tkinter import *
from math import floor
from cell import Cell
from time import sleep


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
        self.draw_cells_frames()

    def draw_cells_frames(self):
        for i in range(9):
            self.cells.append(Cell(i, self))
            self.canvas.create_rectangle(
                i % 3 * self.cell_size + 2, floor(i / 3) * self.cell_size + 2, i % 3 * self.cell_size +
                self.cell_size - 1, floor(i / 3) *
                self.cell_size + self.cell_size - 1,
                fill="white")

    def click_event(self, e: Event):
        # trigger cell click events
        x = floor(e.x / self.cell_size)
        y = floor(e.y / self.cell_size)
        index = y*3+x
        if(not (x < 0 or x > 2 or y < 0 or y > 2)):
            self.cells[index].click_event()
            self.checkWin()

    def checkWin(self):
        # check rows
        for i in range(3):
            state = self.cells[i*3].value
            for j in range(3):
                if(state != self.cells[i*3+j].value):
                    state = ""
            if(state != ""):
                self.ended = True
                self.labelText.set("{} won".format(state))
                self.reset()

        # check cols
        for i in range(3):
            state = self.cells[i].value
            for j in range(3):
                if(state != self.cells[i+j*3].value):
                    state = ""
            if(state != ""):
                self.ended = True
                self.labelText.set("{} won".format(state))
                self.label.update()
                self.reset()

        # check diagonals
        state = self.cells[0].value
        for i in (4, 8):
            if(state != self.cells[i].value):
                state = ""
        if(state != ""):
            self.ended = True
            self.labelText.set("{} won".format(state))
            self.label.update()
            self.reset()

        state = self.cells[2].value
        for i in (4, 6):
            if(state != self.cells[i].value):
                state = ""
        if(state != ""):
            self.ended = True
            self.labelText.set("{} won".format(state))
            self.label.update()
            self.reset()

    def reset(self):
        sleep(1)
        for cell in self.cells:
            cell.value = ""
            cell.draw()
        self.ended = False
        self.turn = "x"
        self.labelText.set("x's turn")
        self.draw_cells_frames()
