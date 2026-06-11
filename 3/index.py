# import math

# name= "John"
# age = 20
# is_new = True

# name = input("WHat is your name? ")
# color = input("Which color do you like? ")

# print(f"{name} likes {color}")


# pounds = input("What is you weight in pounds? ")
# kg = 0.453592 * int(pounds)
# print(f'So you are {kg} kg so better go to gym brooo')




# course ='Python for Beginners'
# print(course.find("P"))
# print(course.replace("o", '0'))



# names = ['ROziya Tukhtayeva', 'Tom Holland', 'Tom Felton', 'Nodirbek Abdusattorov']

# names[0] = 'Son Heung-min'

# print(names)

# numbers = [23,34,45,12]

# maxN = numbers[0]

# # print(len(numbers))
# for number in numbers:
#     if number > maxN:
#         maxN = number
        
# print(maxN)


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]


# for x in matrix:
#     for y in x:
#         print(y)
        
        
# ages = [5,2,4,6,7,4,7,5,3,3,3,3]

# unique = []

# for x in ages:
#     if x not in unique:
#         unique.append(x)
        
# print(unique)

# for a in ages:
#     if  ages.count(a) !=1:
#         ages.remove(a)

# print(ages)



# ages.insert(1,10)
# ages.append(30) #adds the item to the end

# ages.pop() # removes the item in the end

# print(ages.index(4)) # returns the index of that item
# print(ages.count(4)) # counts how many that items in the list
# ages.sort()
# ages.reverse()
# ages2 = ages.copy()
# print(ages2)


# tuples = (1,2,3)
# x,y,z = tuples # unpacking - we can use this feature in others too like list
# print(x*y*z)
# print(tuples[0])


# dictionaries

# costumer = {
#     "name":"Tukhtayeva Roziya",
#     "age": 18,
#     "is_verified": True
# }

# print(costumer["age"])
# print(costumer.get("age1", 20)) # second thing is if the key doesn't have then this thing will be default value
# costumer["name"]='Roziya'
# costumer['birthday'] = '23.08.2008'
# print(costumer["birthday"])

# difference between [''] vs get()
# it does not yell at us if we want to get non existing key

# def number_to_letter(num):
#     match num:
#         case 1:
#             return 'Bir'
#         case 2:
#             return "Ikki"
#         case 3:
#             return "Uch"
#         case 4: 
#             return "Tort"
#         case 5:
#             return "Besh"
#         case 6:
#             return "Olti"
#         case 7:
#             return "Yetti"
#         case 8:
#             return 'Sakkiz'
#         case 9:
#             return 'Toqqiz'
#         case 0:
#             return "Nol"
        
# print(number_to_letter(2))

# n = input("Give me thousand ")
# total = []
# for num in n:
#    print(number_to_letter(int(num)))
#    total.append( number_to_letter(int(num)))
   
# print(total)

# inp = input("Give me thoudsand ")

# digits_mapping = {
#     "1":"Bir ",
#     "2":"Ikki ",
#     "3":"Uch ",
#     "4":"To'rt ",
#     "5":"Besh ",
#     "6":"Olti ",
# }

# output=""

# for n in inp:
#     output +=digits_mapping.get(n,'!')
    
# print(output)


# inp = input('How was your day? ')
# word = inp.split(" ")
# emojis={
#     ":)":"😄",
#     ":(":"😓",
#     "<3":"💚"
# }
# output=""

# for n in word:
#     output+=emojis.get(n,n) +" "
    
# print(output)

# inp = input('How was your day? ')

# def emoji(inp):
#     word = inp.split(" ")
#     emojis={
#         ":)":"😄",
#         ":(":"😓",
#         "<3":"💚"
#     }
#     output=""

#     for n in word:
#         output+=emojis.get(n,n) +" "
#     return output
    
# print(emoji(inp))




# try:
#     age = int(input("Age: "))
#     avarage_p = 100/age
#     print(age)
# except ZeroDivisionError:
#     print("Age can not be 0.")
# except ValueError:
#     print("Please enter number")

# class Chess:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def uzb(self):
#         return "Nodirbek Abdusattorov"
#     def goat(self):
#         print("Magus Carlson")
    
# chess1 = Chess(10,20)
# chess1.smth ='STHHHH'
# chess1.goat()
# print(chess1.x)


# class Person:
#     def __init__(self,name):
#         self.name = name
#     def talk(self):
#         print(f"Hii wassup, I am {self.name}")
        
# person1 = Person("Roziya")

# person1.talk()

# classes are just like C++ I am seeing no difference)


class Action:
    def walk(self):
        print("Walking")
        
class Cat(Action):
    pass

class Dog(Action):
    pass

c = Cat()
c.walk()