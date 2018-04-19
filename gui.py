from tkinter import *
import Mad_Adventure
class Application(Frame):
	def NewWidgets(self):
		self.w = Button(self,text = "New Character", command=self.Startup, bg = 'red', fg = 'white',font = ('times new roman', 20))
		self.q = Button(self,text = "Quit", command = self.quit, bg = 'red', fg = 'white',font = ('times new roman', 20))
		self.title = Message(self, text = "The Mad Mad Adventure", fg = 'blue', bg = 'black', font=('times new roman', 75), width = 1920)
		self.title.pack()
		self.w.pack()
		self.q.pack()
	def input_get(self):
		x = self.e.get()
		print(x)
	def character_name(self):
		string_1 = "Welcome to a world of magic and Adventure!! I require only your name!!" 
		self.s = Text(self)
		self.s.insert(INSERT, string_1)
		self.e = Entry(self)
		self.e.focus()
	def Startup(self):
		self.w.pack_forget()
		self.q.pack_forget()
		self.title.pack_forget()
		self.character_name()
		self.s.pack()
		self.e.pack()
	def __init__(self, master=None):
		Frame.__init__(self, master,width = 1980, height = 1080, bg = 'black')
		self.pack_propagate(0) 
		self.pack()
		self.NewWidgets()
root = Tk()
app = Application(master=root)
app.mainloop()