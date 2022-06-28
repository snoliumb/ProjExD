import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key, cx, cy
    key = event.keysym

def key_up(event):
    global key 
    key = " "

def main_proc():
    global cx, cy, mx, my
    delta = { #キー:押されているキー(key),値:移動幅リスト[x,y]　
        "Up"   :[0, -1],
        "Down" :[0, +1],
        "Left" :[-1, 0],
        "Right":[1, 0],
        }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0: #もし移動先が床なら
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width = 1500, height= 900, bg = "black" )
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file = "fig/1.png")
    cx, cy = 150, 150
    mx, my = 1, 1
    canvas.create_image(cx, cy, image=tori, tag="tori")
    key = " "

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()
