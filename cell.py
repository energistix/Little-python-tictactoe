from tkinter import *
from math import floor
from grid import Grid

class Cell:
    def __init__(self, index: int, grid: Grid) -> None:
        self.value: str = ""
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.canvas: Canvas = grid.canvas
        self.size: int = grid.cell_size
        self.grid: Grid = grid

    def draw(self):
        # drawing the cell based on its value
        if self.value == "o":
            self.canvas.create_oval(self.x * self.size + self.size / 10, self.y * self.size + self.size / 10,
                                    self.x * self.size + self.size / 10 * 9, self.y * self.size + self.size / 10 * 9)
        if self.value == "x":
            self.canvas.create_line(self.x * self.size + self.size / 10, self.y * self.size + self.size / 10,
                                    self.x * self.size + self.size / 10 * 9, self.y * self.size + self.size / 10 * 9)
            self.canvas.create_line(self.x * self.size + self.size / 10 * 9, self.y * self.size + self.size / 10,
                                    self.x * self.size + self.size / 10, self.y * self.size + self.size / 10 * 9)

    def click_event(self):
        # switching states if possible when a user clicks on the cell
        if self.value == "" and (not self.grid.ended):
            self.value = self.grid.turn
            print(self.value)
            self.draw()
            self.grid.turn = ("x", "o")[self.grid.turn == "x"]
            self.grid.labelText.set("{}'s turn".format(self.grid.turn))
