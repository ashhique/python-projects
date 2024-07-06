import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def change_text():
    inp = input_box.get(1.0, "end")
    result_box.delete(1.0, "end")
    result_box.insert(1.0, inp.upper())


window = tk.Tk()
window.title("Convert text to Uppercase")
window.iconbitmap("C:\PycharmProjects\TkinterCalc\img\icons8-note-48.ico")
window.geometry('500x500')

enter_text = tk.Label(window,text="Enter the text here!")
enter_text.pack()

input_box = tk.Text(window, height=5, width=25, bg="light cyan",font=("Helvetica", 10))
input_box.pack()

change_btn = tk.Button(window,text="CHANGE",bg="light pink",command=change_text)
change_btn.pack(pady=7)
Hovertip(change_btn, "Changes text to Uppercase",hover_delay=500)

result_box = tk.Text(window, height=5, width=25, bg="light cyan",font=("Helvetica", 10))
result_box.pack(pady=8)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()