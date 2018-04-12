import tkinter
import Mad_Adventure
top = tkinter.Tk()
# Code to add widgets will go here...
top.title("The Mad Mad Adventure")
f = tkinter.Frame(top, width = 1980, height = 1080, bg = 'black')
b = tkinter.Button(f,text = "New Character", command=Mad_Adventure.character_create, bg = 'red', fg = 'white',font = ('times new roman', 20))
title = tkinter.Message(f, text = "The Mad Mad Adventure", fg = 'blue', bg = 'black', font=('times new roman', 75), width = 1920)
f.pack_propagate(0) 
f.pack()
title.pack()
b.pack()
top.mainloop()
