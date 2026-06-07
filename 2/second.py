x = input("x=")
y = int(x) + 1

print(f'x={x} and y={y}')

temperature = 32

if temperature > 30:
    print("Drink more water")
elif temperature > 20:
    print("warm weather")
else:
    print("smth")
print("DONE")


age = 1
message = 'Hiiii' if age >= 18 else 'Byeee' 
print(message)


high_income = True
spare_time = False
student = True

if high_income and spare_time:
    print("You arwe welcomeee")
else:
    print("SOrryyyyy")

# You know it is the same as && => and 
# || => or

if not student:
    print("WHat are you doing with your life huhhhh")
    print("Actually being a student is not as fun as it looks ngl")
else:
    print("Yay twins")

age = 22

# they have soo good thing its called chain operator
# if you need age between 18 to 65 you probably write

# if age >=18 and age <=65:
# but they have shorter form just like math
# 18 <=age<=65

if 18 <=age <=65:
    print("come on in")
else: 
    print("sorry")

for x in range(1,10,2):
    print("Hi", x, x *".")

# just like for in -> in JS


successful = True

for attemp in range(3):
    print("Attemp")
    if successful:
        print("Successfull")
        break
else:
    print("We tried 3 times but still failed")

for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")

command = ''

while command.lower() != 'quit':
    command = input(">")
    print("ECHO", command)

for x in range(2,10,2):
    print(x)
print("We have  4 even numbers")


def greeting(name, surename):
    print(f"Hellooo {name} {surename}")
greeting("Roziya", surename='Tukhtayeva')
    
def get_greeting(name, age=17):
    return f'Hello {name}, you are {age}'

msg = get_greeting("Roziyaa")
print(msg)


def multiplier(*numbers):
    total = 1
    for x in numbers:
        total *=x
    return total

print(multiplier(2,3,4,5))