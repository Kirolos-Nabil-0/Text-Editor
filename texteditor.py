from Tkinter import *
from tkFileDialog import *


filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfilename(mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
        
    except:
        showerror(title = "Oops!", message = "Unable to save file...")
        
        
def openFile():
    f= askopenfile(mode = 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    
root = Tk()
root.title("K&K Text Editor")
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)

text = Text(root, width = 400, height = 400)
text.pack()

menubar = Menu(root)
filename = Menu(menubar)
filename.add_command(label = "New", command = newFile)
filename.add_command(label = "Open", command = openFile)
filename.add_command(label = "Save", command = saveFile)
filename.add_command(label = "Save As", command = saveAs)
filename.add_separator()
filename.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filename)

root.config(menu = menubar)
root.mainloop()