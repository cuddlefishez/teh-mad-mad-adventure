char = character_create()
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
clearing.monsters.proficiency = monster_info[9]
clearing.monsters.Stats()
clearing.monsters.health = monster_info[6]
clearing.monsters.state = 'alive'
if monster_info[10] == 1:
	clearing.monsters.weapon = weapon_assignment(Weapons,['simple'])
else:
	input("There is a Dragon you dead")
	

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