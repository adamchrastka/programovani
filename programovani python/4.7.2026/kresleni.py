import tkinter
import time
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(145, 125, 255, 195, fill="white")
canvas.create_rectangle(145, 155, 255, 175, fill="blue", outline="")
canvas.create_rectangle(170, 125, 192, 195, fill="blue", outline="")

tkinter.mainloop()