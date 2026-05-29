# Data types
# Number - int, float, complex
# String - str
# Sequence Data - list, tuple, range
# Mapping data - dict
# Set Types - set, frozenset
# Boolean - bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# type() = typeof()

# ----------- Number -----------
# int
year = 2026

#float
weight = 23.8

# complex = bigInt
probability = 1j
print(type(probability)) # complex



# ----------- String -----------
# str
footbal_player = 'Son heung min' 


# ----------- Sequence Data -----------
# list - no special things just like obj 
uzb_chess_players = ['Nodirbek Abdusattorov', 'Javohir Sindarov', 'Nodirbek Yoqubboyev']

# tuple - same as list but with () scope
fav_anime_char =( 'Loid', 'Yor', 'Anya', 'Gojo', 'Taiki')
print(fav_anime_char)

#range - as Math.range in JS only difference is you can tell start, stop and step
#range(start, stop, step)
# if you skip step it will automately will be 1 and if you put only one number then that number will be finishing point and it will start from 0

pets = range(1,5,1)

print(list(pets))

# ----------- Mapping Data -----------
# dict - just like arr in JS
future_goal = {"personality":"curios", "career":"cosmonovt", "home":"Saudia"}

# key must be immutable but we do not care about value - kalit so'z o'zgarmas bo'lishi kerak qiymatlarini farqi yo'q
# I mean list is mutable - Aytmoqchi bo'lganim list o'zgaruvchan shuning uchun key bo'la olmaydi
# no duplicate is allowed
# ordered and changable 
# smth = {[1,2]:"bir ikki"} # error beradi

future_goal['personality'] #we need to call value by key like this not like future_goal.personality

# ----------- Set Types -----------
# set - no duplications, if you add smth twice it will appear only once
# the items are unchangable but you can add and remove it
# the items will be printed unordered like it will show randomly

# the value False and 0  or smth like that treated like a duplicate so one of them will be removed when it was published
# len(set_name) - is equal to set_name.length in JS
# adding 2 sets you need to do 

thisset = {"Harry", 'Draco'}
newOne = {"Hermione", 'Ron'}

thisset.update(newOne) # merging 2 sets
thisset.add("Cedric") # adding to set
thisset.remove("Ron") # if you delete item that doesn't exist then it will raise an error
thisset.remove("Hermione") # if you delete item that doesn't exist then it will NOT raise an error

thisset.pop() # it will remove random item
thisset.clear() # it will clear all items from the set
del thisset # it will remove entire set

print(thisset)

# frozenset it is just like set inaddition you cannot add nor remove anything from it

fs = frozenset({1,2,3,4})
cm = fs.copy() # coping the set
print(cm)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b)) # it will return the difference of these sets
print(a - b) # same here:)))))

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b)) # it will show same values 
print(a & b) # same here:))))


a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b)) # it will say are there any same value in 2 sets return true nor false
print(a.isdisjoint(c)) 


a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b)) # it means a is the main set and b is the part of it if its true then it will return true or false
print(a <= b) # same here
print(a < b) # same here

# Bool

# same as JS