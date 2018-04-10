#this file will contain some sort of combat system I am trying to create that is a bit more complex
# object to create a fighting area
#ie handles all movement throught the combat
#each cell of the array is a 5ft by 5ft square
#this way we can designate battlefeild sizes and movements
#this is going to get integrated with the GUI ASAP 
class arena(object):
	def __init__(self):
		self.width = None
		self.height = None
		self.surface = []
		self.terrain = None
		self.playerpos = None
		self.monsterpos = None
	def arraycreate(self):
	#creates an empty array of correct size
		for n in range(0,self.height):
			self.surface.append([])
		for n in range(0,self.height):
			for m in range(0,self.width):
				self.surface[n].append(0)
	def placement(self):
	#when called places the monsters and resets the array to its base state to allow updates
		a = self.playerpos
		b = self.monsterpos
		self.surface = []
		self.arraycreate()
		self.surface[a[1]][a[0]] = 1
		self.surface[b[1]][b[0]] = 3
	def goto(self):
	#simple function for moving the "player" 
		a = self.playerpos
		j = 1
		while j == 1:
			print("Please select your destination, you are currently at position "+str(self.playerpos)+" the monster is at position "+str(self.monsterpos)+" please make a valid input!")
			r = int(input("Row number"))
			c = int(input("Column number"))
			d = int(((a[0]-r)**2 +(a[1]-c)**2)**.5 // 1 )
			if d*5 >> 300:
				j = 1
				
			else:
				self.playerpos = [r,c]
				self.placement()
				j = -1
				
a = arena()
a.width = 10
a.height = 10
a.playerpos = [8,3]
a.monsterpos = [1,8]
print(a.surface)
a.placement()
print(a.surface)
a.goto()
print(a.surface)