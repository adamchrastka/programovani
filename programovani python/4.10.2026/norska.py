import tkinter as tk
canvas = tk.Canvas()
canvas.pack()
canvas.create_rectangle(100, 100, 255, 195, fill="red")
canvas.create_rectangle(150, 100, 180, 195, fill = "white", outline="")
canvas.create_rectangle(100, 135, 255, 165, fill = "white", outline="")
canvas.create_rectangle(100, 148, 255, 158, fill = "darkblue", outline="")
canvas.create_rectangle(158, 100, 173, 195, fill = "darkblue", outline="")





tk.mainloop()