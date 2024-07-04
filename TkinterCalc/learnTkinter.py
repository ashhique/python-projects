import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Confirm Exit", "Do you want to quit?"):
        window.destroy()


def button_clicked():
    username = username_entry.get()
    entered_user = tk.Label(window, text=f"Username is: {username}", font=("Helvetica", 10))
    entered_user.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)
    password = password_entry.get()
    entered_pass = tk.Label(window, text=f"Password is: {password}", font=("Helvetica", 10))
    entered_pass.pack(side=tk.TOP, anchor=tk.NW, padx=10)


window = tk.Tk()
window.title("Learn Tkinter")
window.iconbitmap("icons8-note-48.ico")
window.geometry('500x500')

username_label = tk.Label(window, text="username:", font=('calibre', 12, 'bold'))
username_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

username_entry = tk.Entry(window, font=("Helvetica", 15))
username_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10)
Hovertip(username_entry, "Enter your username here.", hover_delay=300)

password_label = tk.Label(window, text="password:", font=('calibre', 12, 'bold'))
password_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

password_entry = tk.Entry(window, show="*", font=("Helvetica", 15))
password_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10)
Hovertip(password_entry, "Enter your password here.", hover_delay=300)

submit_button = tk.Button(window, text="check", bd=3, padx=10, pady=7, bg="blue", font=("Helvetica", 10),
                          command=button_clicked)
submit_button.pack(side=tk.TOP, anchor=tk.NW, padx=75, pady=20)
Hovertip(submit_button, "click to Check your username & password", hover_delay=300)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
