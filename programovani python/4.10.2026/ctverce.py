import tkinter as tk
canvas = tk.Canvas()
canvas.pack()
x = 100
y = 100
posuv = 20
canvas.create_rectangle(x, y, x + (posuv * 5), y + (posuv * 5), fill="red")
canvas.create_rectangle(x + 20, y + 20, x + (posuv * 4), y + (posuv * 4), fill="blue")
canvas.create_rectangle(x + 40, y + 40, x + (posuv * 3), y + (posuv * 3), fill="white")


tk.mainloop()