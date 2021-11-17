from tkinter import *
from math import floor
from cell import Cell
from time import sleep
import json

class Grid:
    def __init__(self, window: Tk, cell_size: int) -> None:
        self.cells = []
        self.cell_size = cell_size
        self.window = window
        self.canvas = Canvas(window, height=cell_size*3, width=cell_size*3)
        self.canvas.pack()
        self.canvas.grid(column=0, row=1)
        self.canvas.bind("<Button-1>", self.click_event)
        self.last_turn = "x"
        for i in range(9):
            self.cells.append(Cell(i, self))
        
        # ouverture du fichier de score
        try:
            file = open("./score.json", "r")
            text = file.read()
            file.close()
            self.points = json.loads(text)
        except:
            file = open("./score.json", "w")
            file.write("{\"x\":0, \"o\":0}")
            self.points = {"x": 0, "o": 0}
            file.close()

        # on verifie si self.points contient bien les valeurs nécéssaires (elles aurait pu etre suprimée manuelement par erreur dans le fichier json)
        if not ("x" in self.points):
            self.points["x"] = 0
        if not ("o" in self.points):
            self.points["o"] = 0
        
        self.labelText = StringVar()
        self.labelText.set("x's turn")
        self.label: Label = Label(self.window, textvariable=self.labelText)
        self.label.grid(column=0, row=0)

        self.score_x_text = StringVar()
        self.score_x_text.set("x : {}".format(self.points["x"]))
        self.score_x_label: Label = Label(
            self.window, textvariable=self.score_x_text)
        self.score_x_label.grid(column=1, row=0)

        self.score_o_text = StringVar()
        self.score_o_text.set("o : {}".format(self.points["o"]))
        self.score_o_label: Label = Label(
            self.window, textvariable=self.score_o_text)
        self.score_o_label.grid(column=2, row=0)

        self.restart_button = Button(self.window, text="restart", command=self.reset)
        self.restart_button.grid(column=3, row = 0)

        self.turn = "x"
        self.ended = False
        self.draw_cells_frames()

    def draw_cells_frames(self):
        for i in range(9):
            self.canvas.create_rectangle(
                i % 3 * self.cell_size + 2, floor(i / 3) * self.cell_size + 2, i % 3 * self.cell_size +
                self.cell_size - 1, floor(i / 3) *
                self.cell_size + self.cell_size - 1,
                fill="white")

    def click_event(self, e: Event):
        if self.ended:
            return
        # gestion du click sur la grille
        x = floor(e.x / self.cell_size)
        y = floor(e.y / self.cell_size)
        index = y*3+x
        if not (x < 0 or x > 2 or y < 0 or y > 2):
            self.cells[index].click_event()
            self.check_win()

    def check_win(self):
        # verification des lignes
        for i in range(3):
            state = self.cells[i*3].value
            for j in range(3):
                if state != self.cells[i * 3 + j].value:
                    state = ""
            if state != "":
                self.won(state)

        # verification des collones
        for i in range(3):
            state = self.cells[i].value
            for j in range(3):
                if state != self.cells[i + j * 3].value:
                    state = ""
            if state != "":
                self.won(state)

        # verification des diagonales
        state = self.cells[0].value
        for i in (4, 8):
            if state != self.cells[i].value:
                state = ""
        if state != "":
            self.won(state)

        state = self.cells[2].value
        for i in (4, 6):
            if state != self.cells[i].value:
                state = ""
        if state != "":
            self.won(state)
        
        # verification des égalités
        full = True
        for cell in self.cells:
            if(cell.value == ""):
                full = False
        if(full):
            self.reset()

    def reset(self):
        # remise a 0 de la grille
        for cell in self.cells:
            cell.value = ""
            cell.draw()
        self.ended = False
        self.last_turn = ("x", "o")[self.last_turn == "x"]
        self.turn = self.last_turn
        self.labelText.set("{}'s turn".format(self.turn))
        self.draw_cells_frames()

    def won(self, state):
        # gestionde la victoire
        self.ended = True
        self.points[state] += 1
        self.labelText.set("{} won".format(state))
        self.label.update()
        self.update_score()

    def update_score(self):
        # modification des labels et du fichier de score avec les nouveaux scores
        self.score_o_text.set("o : {}".format(self.points["o"]))
        self.score_x_text.set("x : {}".format(self.points["x"]))
        file = open("./score.json", "w")
        file.write(json.dumps(self.points))
