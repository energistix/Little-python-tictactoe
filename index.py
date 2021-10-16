from tkinter import *
from grid import Grid
window = Tk()


grid = Grid(window, 100)
window.bind("<Button-1>", grid.click_event)
window.mainloop()
