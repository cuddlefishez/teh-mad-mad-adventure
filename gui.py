from tkinter import *
import Mad_Adventure
class Application(Frame):
	def __init__(self, master=None):
	#standard __init__ function
		Frame.__init__(self, master,width = 1980, height = 1080, bg = 'black')
		self.pack_propagate(0) 
		self.pack()
		self.NewWidgets()
	def NewWidgets(self):
	#creates base widgets on start menu
		self.w = Button(self,text = "New Character", command=self.Startup, bg = 'red', fg = 'white',font = ('times new roman', 20))
		self.q = Button(self,text = "Quit", command = self.quit, bg = 'red', fg = 'white',font = ('times new roman', 20))
		self.title = Message(self, text = "The Mad Mad Adventure", fg = 'blue', bg = 'black', font=('times new roman', 75), width = 1920)
		self.title.pack()
		self.w.pack()
		self.q.pack()
	def character_name(self):
	#sets the stage for collecting character name
		string_1 = "Welcome to a world of magic and Adventure!! I require only your name:!!" 
		self.s = Text(self, width = len(string_1), height = 1,background = 'black', foreground = 'white',relief= FLAT)
		self.s.insert(INSERT, string_1)
		self.e = Entry(self)
		self.e.focus()
		self.s.pack()
		self.e.pack()
		self.e.bind("<Return>", self.input_get)
	def input_get(self,*args):
	#this function collects the input and creates the character upon hitting enter
		name = self.e.get()
		char = Mad_Adventure.Player()
		char.name = name
		print(char.name)
	def Startup(self):
	#clears the frame, will put a loading screen here in future
		self.w.pack_forget()
		self.q.pack_forget()
		self.title.pack_forget()
		self.character_name()
root = Tk()
app = Application(master=root)
app.mainloop()
