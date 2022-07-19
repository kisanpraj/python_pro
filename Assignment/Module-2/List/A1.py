#Write a Python prog to select an item randomly from a list?

#Ans==>

from random import choice

def random_ele(lst):
    return choice(lst)
print(random_ele([1,2,3,4,5,6,7]))

import random
color=['red','blue','black','white','green']
print(random.choice(color))