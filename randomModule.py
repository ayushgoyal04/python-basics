import random

x = random.randint(1,6) # random integer between 1 and 6
y = random.random() # random float number between 0 and 1
print(x)
print(y)
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

random.shuffle(cards)
print(cards)