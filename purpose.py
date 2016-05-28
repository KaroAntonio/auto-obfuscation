import random

def giveUp():
	pass

def searchForGod( where = 'here' ):
	if where == 'inside':
		return 'me'
	else: return 'you'

def code( time = int(random.random() * 100) ):
	print('help im lost')
	if time > 0:
		time -= 1
		code( time )

def eatPopcorn():
	bucket = ["salty" for i in range(int(random.random() * 20))]
	face = []
	for popcorn in bucket:
		face += [ popcorn ] 

def callEx():
	important_things_to_say = [
			'I never told you youre the only person to make me cry',
			'How come you never looked me in the eyes after sex?',
			'how long did you love me for before evaporating'
			]
	inertia = 0
	if inertia != 0:
		for thing in important_things_to_say:
			print thing

def tinder():
	swipes = 30
	while swipes > 0:
		pic_of_other = " ;) "
		if pic_of_other == "ex":
			print "swipe left"
		else: print "swipe right"
		swipes -= 1

purpose = None
while purpose == None:
	purpose = random.choice([
		giveUp,
		callEx,
		code,
		eatPopcorn,
		tinder,
		searchForGod,
		])()
	print(purpose)
	if purpose != "what im looking for":
		purpose = None
