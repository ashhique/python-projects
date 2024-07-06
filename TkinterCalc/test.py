import tkinter as tk

def toggle_status():
    if status_var.get():
        print("Status bar enabled")
    else:
        print("Status bar disabled")

def toggle_word_wrap():
    if word_wrap_var.get():
        print("Word wrap enabled")
    else:
        print("Word wrap disabled")

window = tk.Tk()
window.title("Notepad demo")
window.geometry("500x500")

menubar = tk.Menu(window)

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New tab")
filemenu.add_command(label="New window")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as")
filemenu.add_command(label="Save all")
filemenu.add_separator()
filemenu.add_command(label="Page setup")
filemenu.add_command(label="Print")
filemenu.add_separator()
filemenu.add_command(label="Close tab")
filemenu.add_command(label="Close window")
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_separator()
editmenu.add_command(label="Search with Bing")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Find next")
editmenu.add_command(label="Find previous")
editmenu.add_command(label="Replace")
editmenu.add_command(label="Go to")
editmenu.add_separator()
editmenu.add_command(label="Select all")
editmenu.add_command(label="Date/Time")
editmenu.add_separator()
editmenu.add_command(label="Font")
menubar.add_cascade(label="Edit", menu=editmenu)

# View menu
viewmenu = tk.Menu(menubar, tearoff=0)

status_var = tk.BooleanVar()
status_var.set(True)
viewmenu.add_checkbutton(label="Status bar", variable=status_var, command=toggle_status)

word_wrap_var = tk.BooleanVar()
word_wrap_var.set(False)
viewmenu.add_checkbutton(label="Word wrap", variable=word_wrap_var, command=toggle_word_wrap)

viewmenu.add_command(label="Zoom")
menubar.add_cascade(label="View", menu=viewmenu)

# Attach the menu bar to the window
window.config(menu=menubar)

window.mainloop()
