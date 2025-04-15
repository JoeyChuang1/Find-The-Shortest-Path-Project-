# main.py

import sys
import os
import pygame
from tkinter import Tk, Label, Entry, IntVar, Button, ttk
from pathfinding.grid import Grid
from visualization.pygame_visual import PygameVisualizer

def onsubmit():
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start_pos = (int(st[0]), int(st[1]))
    end_pos = (int(ed[0]), int(ed[1]))
    window.quit()
    window.destroy()
    visualizer = PygameVisualizer(grid_size=(50, 50), start=start_pos, end=end_pos, show_steps=var.get())
    visualizer.run()

# Tkinter GUI for user input
window = Tk()
window.title("Pathfinding Input")
Label(window, text='Start(x,y): ').grid(row=0, pady=3)
startBox = Entry(window)
startBox.grid(row=0, column=1, pady=3)
Label(window, text='End(x,y): ').grid(row=1, pady=3)
endBox = Entry(window)
endBox.grid(row=1, column=1, pady=3)
var = IntVar()
ttk.Checkbutton(window, text='Show Steps:', onvalue=1, offvalue=0, variable=var).grid(columnspan=2, row=2)
Button(window, text='Submit', command=onsubmit).grid(columnspan=2, row=3)
window.mainloop()
