# Data types
# Number - int, float, complex
# String - str
# Sequence Data - list, tuple, range
# Mapping data - dict
# Set Types - set, frozenset

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

# smth = {[1,2]:"bir ikki"} # error beradi

future_goal['personality'] #we need to call value by key like this not like future_goal.personality

