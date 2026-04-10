import tkinter as tk
canvas = tk.Canvas()
canvas.pack()
canvas.create_rectangle(20, 50, 30, 150, fill="blue")
canvas.create_rectangle(20, 50, 190, 60, fill="red")
canvas.create_rectangle(180, 50, 190, 150, fill="blue")
canvas.create_rectangle(30, 150, 190, 140, fill="red")

tk.mainloop()