from random import choice
from random import randint

#adjective 1
l0 = ['Super', 'Infinitely', 'Mega']
#adjective 2
l1 = ['Real', 'Cute', 'Adorable', 'Kawaii', 'Fake', 'Pretty', 'Pink', 'Strong', 'Weak', 'Funny', 'Sad', 'Angry']
#noun
l2 = ['Mitochondria', 'Dude', 'Ghost', 'Waifu', 'Boss', 'Killer', 'Stalin', 'Comrade', 'Putin', 'Obama', 'Bernie']

#randomizes the three lists
def nameg():
    a = randint(0, 5)
    n1 = choice(l1)
    n2 = choice(l2)
    if a == 3:
        return choice(l0) + n1 + n2
    return n1 + n2
    

