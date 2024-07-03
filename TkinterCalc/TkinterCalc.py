import tkinter as tk

def clicked(event):
    now = display.get()
    text = event.widget.cget('text')

    if text == "=":
        result = eval(now)
        display.delete(0,tk.END)
        display.insert(tk.END,result)
    elif text == "C":
        display.delete(0,tk.END)
    else:
        display.insert(tk.END, text)

window = tk.Tk()
window.title("Calculator")
display = tk.Entry(window, font=("Arial",25), justify="right", bd=4)
display.pack(fill=tk.X,padx=10,pady=10,ipady=15)

button_frame = tk.Frame(window)
button_frame.pack()

button_labels = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "C","0","=","/"
]

i=0
for label in button_labels:
    button = tk.Button(button_frame,text=label,font=("Arial",18),padx=20, pady=20)
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind("<Button-1>",clicked)
    i+=1
window.mainloop()