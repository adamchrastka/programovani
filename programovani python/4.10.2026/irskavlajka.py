import tkinter as tk
canvas = tk.Canvas()
canvas.pack()
canvas.create_rectangle(145, 125, 255, 195, fill="white")
canvas.create_rectangle(145, 125, 180, 195, fill = "green")
canvas.create_rectangle(220, 125, 255, 195, fill = "orange")
tk.mainloop()