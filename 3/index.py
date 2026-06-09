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
        
        
ages = [5,2,4,6,7,4,7,5,3,3,3,3]

unique = []

for x in ages:
    if x not in unique:
        unique.append(x)
        
print(unique)

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

costumer = {
    "name":"Tukhtayeva Roziya",
    "age": 18,
    "is_verified": True
}

print(costumer["age"])