import random
import string
# the class below is the room code meant for creating rooms in dungeons and open world for the player to interact 
class Room(object):
	def __init__(self):
		self.initial_text = None
		self.mchecks = None
		self.schecks = None
		self.choices = None
		self.monsters = None
		self.objects = None
		self.traps = None
		self.actions = None
"""
The array below will hold the different pointers for the encounter tables currently only one entry
someone will have to create tables for encounters so we have custom ones for every area
"""
table_dict = {'plains':3}
keyed_dict = {3: [{ 1:'Goblin'},{2:'Hobgoblin'},{3:'Ancient Black Dragon'}]}

# this class creates combat instances, not sure if I still want it to be this way, however it may be the best way to add story combats 
class Combat(object):
	def __init__(self):
		self.player = None
		self.Monsters = None
		self.intiative = None
	def Fight(self):
		m = 1
		while m == 1:
			for x in self.intiative:
				if x in self.Monsters:
					k = x.Attack()
					if k[0] >= self.player.AC:
						y = x.Dmg(k[1])
						print ('The '+str(x.name)+' strikes you for '+str(y)+' damage!')
						self.player.TakeDmg(y)
						if self.player.state == 'dead':
							print("You lose!!!!")
							m = 3
							break
						else:
							continue
					else:
						print ('You manage to pull your '+str(self.player.weapon)+' to your defence and parry the strike!')
				else:
					mans = []
					l = ''
					for mon in self.Monsters:
						mans.append(mon.name)
					while l not in mans:
						l = input("Your time to strike is now! Which monster will you attack!"+str(mans))
					for mon in self.Monsters:
						if mon.name == l:
							monst = mon
						else: 
							continue
					k = x.Attack()
					if k[0] >= monst.AC:
						y = x.Dmg(k[1])
						print ('Your strike is true! You do '+str(y)+' damage to the '+str(monst.name)+'!')
						monst.TakeDmg(y)
						if monst.state == 'dead':
							print("You won!!!!!!!")
							m = 3
							break
						else:
							continue
					else:
						print('You missed!')
	
# before this comment need to write a piece of code to find the combat order from the dictionary and sort it into a two dimensional array 
#here we need to set up a system for clicking on the monster they wish to attack or at least have a sequence of buttons
#we want to check the conditions of the fight, so how much range the weapon has, which monsters are within range, all that jazz
#movement should be set up a bit like a chess board	
# here is mainly just calling info from turn order, then having each monster ai choose what it wants to do 

class Monster(object):
	def __init__(self):
		self.name = None
		self.AC = None
		self.health = None
		self.state = None
		self.proficiency = None
		self.weapon = None
		self.CR = None
		self.str = None
		self.dex = None
		self.con = None
		self.int = None
		self.wis = None
		self.cha = None
		self.stats = None
	def Stats(self):
		self.stats = {'Strength': self.str,'Dexterity':self.dex,'Constitution':self.con,'Intellegence':self.int,'Wisdom':self.wis,'Charisma':self.cha}
	def Attack(self):
		c = 0
		roll = twenty.Roll()
		if roll == 20:
			c = 1
			print("A dangerous strike!")
		mod = ((self.str-10)/2)//1
		x = roll + mod 
		return(int(x),c)
	def Dmg(self,c):
		x = weapon_info(self.weapon,Weapons)
		if self.weapon == 'Fist':
			dmg = 1 + ((self.str-10)/2)//1
		else:
			dmg = x[1][1][1].Roll() + ((self.str-10)/2)//1
		
		return(dmg*(c+1))
	def TakeDmg(self,dmg):
		self.health = self.health - dmg
		if self.health <= 0:
			self.state = 'dead'
		else:
			self.state = 'alive'
		
		
		
	
# this is the player class which holds and keeps the player state	
class Player(object):
	def __init__(self):
		self.name = None
		self.level = None
		self.stats = None
		self.player_class = None
		self.hitdice = None
		self.health = None
		self.inventory = []
		self.weapon = None
		self.spells = []
		self.money = {'gp': 0, 'sp': 0, 'cp': 0}
		self.AC = None
		self.initiative = None
		self.state = None
		self.proficiency = None
	def Access_Inv(self):
		print(self.inventory)
		input("Is there something you would like to grab?")
	def Check_Health(self):
		print(self.health)
	def Summary(self):
		self.Check_Health()
		self.Access_Inv()
		print(self.stats)
	def Attack(self):
	# handles player attacks
		c = 0
		roll = twenty.Roll()
		if roll == 20:
			c = 1
			print("That's a critical strike!!")
		mod = ((self.stats['Strength']-10)/2)//1
		x = roll + mod 
		return(int(x),c)
	def Dmg(self,c):
	#handles player dmg
		x = weapon_info(self.weapon,Weapons)
		if self.weapon == 'Fist':
			dmg = 1 + ((self.stats['Strength']-10)/2)//1
		else:
			dmg = x[1][1][1].Roll() + ((self.stats['Strength']-10)/2)//1
		
		return(dmg*(c+1))
	def TakeDmg(self,dmg):
	#handles dmg recieved
		self.health = self.health - dmg
		if int(self.health) <= 0:
			print('You are dead')
			self.state = 'dead'
		else:
			print('You have '+str(self.health)+' remaining')
	def starting_gold(self):
	#gives starting gold
		gold = {'Barbarian': [2,four,10] ,'Bard': [5,four,10],'Cleric':[5,four,10],'Druid':[2,four,10],'Fighter':[5,four,10],'Monk':[5,four,1],'Paladin':[5,four,10],'Ranger':[5,four,10],'Rogue':[4,four,10],'Sorcerer':[3,four,10],'Warlock':[4,four,10],'Wizard':[4,four,10]}
		g = gold[self.player_class]
		gp = int(g[1].multiRoll(g[0])*g[2])
		self.money['gp'] = gp
	def Alive(self):
		if self.state == 'dead':
			print('You Are Dead')
#Below are the dice objects used to generate random numbers!! You can make as many as you want!!
class d20(object):
	def __init__(self):
		self.roll = 0
	def Roll(self):
		self.roll = random.randint(1,20)
		return(self.roll)
class d12(object):
	def __init__(self):
		self.roll =0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,12)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n+1):
			x = self.Roll()
			self.total += x
		return(int(self.total))
class d10(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,10)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n+1):
			x = self.Roll()
			self.total += x
		return(int(self.total))
class d8(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,8)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n+1):
			x = self.Roll()
			self.total += x
		return(int(self.total))
class d6(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,6)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n+1):
			x = self.Roll()
			self.total += x
		return(int(self.total))
class d4(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,4)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n+1):
			x = self.Roll()
			self.total += x
		return(int(self.total))
class d100(object):
	def __init__(self):
		self.roll = 0
	def Roll(self):
		self.roll = random.randint(1,100)	
		return(self.roll)
Stat_Names = ['Strength', 'Constitution', 'Dexterity', 'Intellegence', 'Wisdom', 'Charisma']	
def player_iniative(Player):
	x = input("You have enter combat! Roll for initative!!")
	r = skill_check('Dexterity',Player.stats,0,0)
	return(r)

def monster_iniative(Monster):
	r = monster_check(Monster,'Dexterity')
	return(r)

	
def intiative_order(monsters,player):
	keydict = {}
	initative= []
	for monster in monsters:
		x = monster_iniative(monster)
		keydict[x] = monster
		initative.append(x)
	p = player_iniative(player)
	keydict[p] = player 
	initative.append(p)
	initative.sort()
	initative.reverse()
	order = []
	for i in initative:
		order.append(keydict[i])
	return(order)

def weapon_assignment(Weapons,choice):
	# Weapons is list
	# Choice is string list to expand choice of weapon based on type shown below in access_lv this function is mearly
	# to introduce random weapons to enemys and the player, a shop will be set up for starting equipment inchar creation
	access_lv = {'simple':0, 'simple_r':1,'martial':2,'martial_r':3}
	a = []
	weap = []
	for choice in choice:
		a.append(access_lv[choice])
	for n in a:
		weap.append(Weapons[n][random.randint(1,len(Weapons[n])-1)][0])
	weapon = weap[random.randint(0,len(weap)-1)]
	return(weapon)
def weapon_shop_inital(Weapons,choice):
	access_lv = {'simple':0, 'simple_r':1,'martial':2,'martial_r':3}
	a = []
	weap = []
	for choice in choice:
		a.append(access_lv[choice])
	for n in a:
		for l in range(1,len(Weapons[n])):
			weap.append(Weapons[n][1][0])
	return(weap)
def weapon_info(weapon,Weapons):
	#weapon is a string
	#Weapons is a multi dimensional list
	for a in range(0, len(Weapons)):
		for l in Weapons[a]:
			if weapon in l:
				k = l 
			else:
				continue
	return(k)
def Stat_Roller(): 
#stat roller function for character creation currently curved to higher stats
	stat = random.randint(3,6) + random.randint(3,6) + random.randint(3,6)
	return(stat)
def Stat_Assignment():
# stat assignment function for character creation 
	Abillity_Score = {'Strength': 1,'Dexterity': 1, 'Constitution': 1,  'Intellegence': 1, 'Wisdom': 1, 'Charisma': 1}
	stats = []
	for i in range(0,6):
		stats.append(Stat_Roller())
	print(stats)
	m = 'normal'
	for stat in Stat_Names:
		j = 1
		while j == 1:
			if m == "auto":
				stats.sort()
				stats.reverse()
				k = stats[0]
				stats.remove(int(k))
				Abillity_Score[stat] = k
				j = -1
			else:
				i1 = input('Which number would you like to assign to the '+stat+' score or press 1 for auto! ')
				try:
					i1 = int(i1)
				except ValueError:
						print('')
				if i1 in stats:
					stats.remove(int(i1))
					Abillity_Score[stat] = i1
					j = -1
				elif i1 == 1:
					stats.sort()
					stats.reverse()
					k = stats[0]
					stats.remove(int(k))
					Abillity_Score[stat] = k
					j = -1
					m = 'auto'
				else:
					print('Please try again your unassigned values are '+str(stats)+' ! ')		
	return(Abillity_Score)
def player_class():
# function to determine the class a player wants to play
	player_class = ''
	playable = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
	j = 1
	while j == 1:
		i2 = str(input('There are '+str(len(playable))+' classes in this game, please choose one from this list '+str(playable)+' ... '))
		if string.capwords(i2) in playable:
			i3 = input('You have picked the '+string.capwords(i2)+' class, are you sure about playing this class? ')
			if i3.lower() == 'yes':
				player_class = string.capwords(i2)
				j = -1
			else:
				print('Please choose your desired class!')
		else:
			print('Your input is invalid, please try again!')
	return(player_class)
def hitdice(player_class):
#hit dice values for each class 
	hitdice = ''
	d12 = ['Barbarian']
	d10 = ['Cleric','Fighter','Paladin']
	d8 = ['Bard','Druid','Rogue','Ranger','Warlock','Monk']
	d6 = ['Wizard','Sorcerer']
	dice = [d12,d10,d8,d6]
	dicevalue = ['d 12','d 10','d 8','d 6']
	k = 0
	for hdice in dice:
		if player_class in hdice:
			hitdice = dicevalue[k]
			break
		else:
			k += 1
	return(hitdice)
def health(level,stats,hitdice):
# basic health calculation 
	mod = ((stats['Constitution']-10)/2)//1
	jank = hitdice.split()
	value = int(jank[1])
	if level == 1:
		health = value + mod
	else:
		health = health + random.randint(1,value)+ mod
	return(int(health))
def encounter(place):
	#place is a string based on room later will add difficulty setting
	list = keyed_dict[table_dict[place]]
	roll = hundred.Roll()
	if roll <= 50:
		key = 1
	elif roll > 50 and roll != 100:
		key = 2
	else: 
		key =3
	monster = list[key-1][key]
	return(str(monster))
"""
The next dictionary is a doozy, it will contain all of the monsters and all of thestats
so for stats order is str, dex, con, int, wis, cha, health, CR, AC , proficiency,weapon
"""	
monster_dict = {'Goblin':[8,14,10,10,8,8,7,0.25,15,2,1],'Hobgoblin':[13,12,12,10,10,9,11,.5,18,2,1],'ElderBlackDragon':[27,14,25,16,15,19,367,21,22,7,0]}


hundred = d100()
twenty = d20()
twelve = d12()
ten = d10()
eight = d8()
six = d6()
four = d4()
"""
The following list is a classification of weapontypes it is a multidimensional array
first the weapon classification as simple, simple ranged, martial or martial ranged acts as a pointer
then the weapon name points to ward the particular properties of that weapon as follows, cost, damage dice, damage type 
(b for blugeoning, s for slashing, p for piercing), weight in lbs., any other specific properties 
note: in specific properties thrown1 is an indication of range (20,60) ft thrown2 is indication of (30,120) ft
"""
Weapons = [['simple',['Club',[[1,'sp'],[1,four],'b',2,['light']]],['Dagger',[[2,'gp'],[1,four],'p',1,['finesse','light','thrown1']]],['Greatclub',[[2,'sp'],[1,eight],'b',10,['two-handed']]],['Handaxe',[[5,'gp'],[1,six],'s',2,['light','thrown1']]],['Javalin',[[5,'sp'],[1,six],'p',2,['thrown2']]],['Light-Hammer',[[2,'gp'],[1,four],'b',2,['light','thrown1']]],['Mace',[[5,'gp'],[1,six],'b',4,['Light']]],['Quaterstaff',[[2,'sp'],[1,six],'b',4,['versatile']]],['Sickle',[[1,'gp'],[1,four],'s',2,['light']]],['Spear',[[1,'gp'],[1,six],'p',3,['thrown1','versatile']]],['Fist',[[0,''],1,'b','','']]],['simple_r'],['martial'],['martial_r']]
def skill_check(stat, stats, proficiency,bonus):
#player skill checks 
	mod = ((stats[stat]-10)/2)//1
	x = twenty.Roll()
	check = x + mod + proficiency + bonus
	return(int(check))
def monster_check(monster,stat):
#stat must be string (Dexterity,so on)
#monster skill checks currently broken
	
	mod = ((monster.stats[stat]-10)/2)//1
	x = twenty.Roll()
	check = x + mod 
	return(int(check))
print('Welcome to a world of magic and Adventure! Befor we jump in there are few things that you must answer me!')
char = Player()
char.name = input('I require only your name! The rest is up to you! ')
char.level = 1
char.player_class = player_class()
char.starting_gold()
char.hitdice = hitdice(char.player_class)
char.stats = Stat_Assignment()
char.weapon = weapon_assignment(Weapons,['simple'])
print(char.weapon)
char.inventory = ['Rations5','Bedroll','Firestarter']
char.health = health(char.level, char.stats, char.hitdice)
char.AC = 10 + ((char.stats['Dexterity']-10)/2)//1
char.state = 'alive'

print('Well done '+char.name+' now there are only a few more questions you must answer!')
print(char.money['gp'])
clearing = Room()
clearing.initial_text = 'Its been seven days since you set out from your small town to make for the city of Whitewater. Last night you decided to camp off the road. It is early morning now, roll perception!'
clearing.mchecks = {'Perception' : 15}
clearing.monster = encounter('plains')
monster_info = monster_dict[clearing.monster]
clearing.monsters = Monster()
clearing.monsters.name = clearing.monster
clearing.monsters.str = monster_info[0]
clearing.monsters.dex = monster_info[1]
clearing.monsters.con = monster_info[2]
clearing.monsters.int = monster_info[3]
clearing.monsters.wis = monster_info[4]
clearing.monsters.cha = monster_info[5]
clearing.monsters.AC = monster_info[8]
clearing.monsters.Stats()
clearing.monsters.health = monster_info[6]
clearing.monsters.state = 'alive'
if monster_info[10] == 1:
	clearing.monsters.weapon = weapon_assignment(Weapons,['simple'])
else:
	input("There is a Dragon Nigger you dead")
	

clearing.actions = ['Roll Perception','']

#here I want to have a function that creates monsters, like pulls stats from the book and does a bit of random health rolling
#RELATED NOTE!! IN ANOTHER FILE WE SHOULD MAKE A WEAPON ASSIGNMENT FUNCTION FOR MONSTERS!! 

clearing.mchecks['Perception'] = twenty.Roll()+20
j = 1
while j == 1:
	action_input = input(clearing.initial_text)
	if string.capwords(action_input) in clearing.actions:
		x = skill_check('Wisdom',char.stats,0,0)
		if x >> clearing.mchecks['Perception']:
			link = 1
			j = -1
		else:
			link = 2
			j = -1
	else:
		print('That is not a valid action, you may '+str(clearing.actions)+' ...')
clearing1 = Room()
if link == 1:
	clearing1.initial_text = 'Your eyes open to a slight shuffling behind you, turning around you notice that a'+str(clearing.monsters.name)+'has infiltrated your campsite!'
	clearing1.monsters = clearing.monsters.name
	clearing1.actions = ['Attack']
	print(clearing1.initial_text)
	print(str(clearing1.actions))
elif link == 2:
	x = hundred.Roll()
	if x <= 2: 
		clearing1.initial_text = 'You continue to peacefully sleep, the only thing that rouses you is the chirping of birds several hours later'
		char.gold = 0
		char.weapon = ['Fist']
		char.inventory = []
		link = 'a1'
		print(clearing1.initial_text)
	else: 
		clearing1.initial_text = 'You hear a shout and open your eyes to a '+clearing.monsters.weapon.lower()+' coming down toward you'
		link = 'a2'
if link == 'a2':
	
	
	monsters = [clearing.monsters]
	print(clearing1.initial_text)
	a = intiative_order(monsters,char)
	c = Combat()
	c.intiative = a 
	c.player = char 
	c.Monsters = monsters
	c.Fight()
	
	
	
