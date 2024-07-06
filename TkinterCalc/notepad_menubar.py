import tkinter as tk

window = tk.Tk()
window.title("Menubar Demo")
window.geometry("500x500")

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff=0)

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

menubar.add_cascade(label="File",menu=filemenu)

editmenu = tk.Menu(menubar,tearoff=0)

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

menubar.add_cascade(label="Edit",menu=editmenu)

viewmenu = tk.Menu(menubar,tearoff=0)

zoom_menu = tk.Menu(viewmenu,tearoff=0)
zoom_menu.add_command(label="Zoom in")
zoom_menu.add_command(label="Zoom out")
zoom_menu.add_command(label="Restore default zoom")
viewmenu.add_cascade(label="Zoom",menu=zoom_menu)

viewmenu.add_checkbutton(label="Status bar",offvalue=1)
viewmenu.add_checkbutton(label="Word wrap",offvalue=1)
menubar.add_cascade(label="View",menu=viewmenu)

window.config(menu=menubar)

window.mainloop()