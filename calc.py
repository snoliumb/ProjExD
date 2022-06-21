import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}のボタンがクリックされました。")
    entry.insert(tk.END,num)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("400x630")
    r, c = 2,0
    for num in range(9, -1, -1):
        btn = tk.Button(root,
                        text=f"{num}",
                        width=4,
                        height=2,
                        font=("Times New Roman", 30)
                   ) 
        btn.grid(row=r, column=c) 
        c += 1
        if (num-1)%3 ==0:
            r += 1
            c = 0 
        btn.bind("<1>", button_click)
    entry = tk.Entry(width=30)
    entry.grid(columnspan=2, row=1, column = 1)
    root.mainloop()
