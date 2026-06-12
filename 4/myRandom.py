import random

for i in range(3):
    print(random.random()) 
    # just like random in JS (it shows number from 0 to 1)
    print(random.randint(1,10)) 
    # also like random but it shows between number 
    
    
memebers = ['Taiki', 'Chinatsu',"Hina", "Kyo"]

print(random.choice(memebers))

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print(f"({dice1}, {dice2})")

class Dice:
    def roll(self):
        tuple1 = (1,2,3,4,5,6)
        tuple2 = (1,2,3,4,5,6)
        return f"({random.choice(tuple1)}, {random.choice(tuple2)})"

d = Dice()    
print(d.roll())