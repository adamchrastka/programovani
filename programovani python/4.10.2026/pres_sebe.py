import tkinter as tk
canvas = tk.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 150, 150, fill="blue")
canvas.create_rectangle(70, 70, 170, 170, fill="red")
canvas.create_rectangle(90, 90, 190, 190, fill="pink")
canvas.create_rectangle(110, 110, 210, 210, fill="yellow")

tk.mainloop()