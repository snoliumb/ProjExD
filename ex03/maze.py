import tkinter as tk
import tkinter.messagebox as tkm
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width = 1500, height= 900, bg = "black" )
    canvas.pack()
    root.mainloop()
