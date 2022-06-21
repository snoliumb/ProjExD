import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}のボタンがクリックされました。")
    if num == "=":
        a = entry.get()
        b = eval(a)
        entry.delete(0, tk.END)
        entry.insert(0,b)
    elif num == "AC":
        entry.delete(0, tk.END)
    elif num == "C":
        l = entry.get()
        n = len(l)
        entry.delete(n-1, tk.END)
    elif num == "/x":
        a = entry.get()
        b = eval(a)
        c = 1/b
        entry.delete(0, tk.END)
        entry.insert(0,c)
    elif num == "x*2":
        a = entry.get()
        b = eval(a)
        c = b * b
        entry.delete(0, tk.END)
        entry.insert(0,c)
    elif num == "√":
        a = entry.get()
        b = eval(a)
        c = b ** (1/2)
        entry.delete(0, tk.END)
        entry.insert(0,c)
    else:
        entry.insert(tk.END,num)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("600x930")
    r, c = 6, 0
    for num in range(1, 10):
        btn = tk.Button(root,
                        text=f"{num}",
                        width=4,
                        height=2,
                        font=("Times New Roman", 30)
                   ) 
        btn.grid(row=r, column=c) 
        c += 1
        if num%3 ==0:
            r -= 1
            c = 0 
        btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="0",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=7, column=1)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="+",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=7, column=2)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="=",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=7, column=3)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="-",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=4, column=3)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="*",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=5, column=3)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="/",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=6, column=3)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="(",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=3, column=2)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text=")",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=3, column=3)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="AC",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=3, column=1)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="C",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=3, column=0)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="/x",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=3, column=4)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text=".",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=7, column=0)
    btn.bind("<1>", button_click)

    btn = tk.Button(root,
                    text="x*2",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=4, column=4)
    btn.bind("<1>", button_click)
    
    btn = tk.Button(root,
                    text="√",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                   ) 
    btn.grid(row=5, column=4)
    btn.bind("<1>", button_click)

    entry = tk.Entry(width=30)
    entry.grid(columnspan=2, row=1, column = 1)
    root.mainloop()
