# -------------------- reading method --------------------
# def read_file():
#   file = open('characters.txt', 'r')
#   content = file.read()
#   print(content)
#   file.seek(0)
#   lines = file.readlines()
#   for line in lines:
#     print(line)
    
#   file.close()
  
# read_file()


# -------------------- writing method --------------------

# characters = ['Kira', 'L', 'Misa', 'Ryuk', 'Rem']

# def write_file(filename):
#   file = open(filename, 'w+')
#   for ch in characters:
#     file.write(ch+ '\n')
#   file.seek(0)
#   content = file.read()
#   print(content)

# write_file("wcharacter.txt")

# -------------------- adding method --------------------
# more_characters= ['Harry', 'Hermione', 'Draco', 'Ron', 'Luna', ]

# def adding_to_file(filename):
#   file = open(filename, 'a+')
#   for ch in more_characters:
#     file.write(ch+"\n")
#   file.seek(0)
#   content = file.read()
#   print(content)
  
# adding_to_file("wcharacter.txt")  

# -------------------- creating folder method --------------------

# from pathlib import Path

# def create_path():
#   path = Path(__file__).parent / 'do' / 'not' / 'exist.txt'
#   try:
#     file=path.open('r')
#     print(file.read())
#   # except FileNotFoundError:
#   #   print(f'{path} do not exist')
#   except Exception as e:
#     print(f"Error: {e}")
#   print("End")
#   # script_dir = Path(__file__).parent
#   # path = script_dir / 'smth'
#   # path.mkdir(parents=True, exist_ok=True)
#   # path = path / 'zelda.txt'
#   # # file = path.open('r')
#   # # content = file.read()
#   # # print(content)
#   # # file.close()
#   # content=path.read_text()
#   # print(content)
  
# create_path()


# from pathlib import Path

# def open_file():
#   path = Path(__file__).parent / 'smth.txt'
#   data = ['Avocado', 'Pink', 'Alt']
#   with path.open("a+") as file:
#     for randm in data:
#       file.write(randm + "\n")
#     file.seek(0)
#     print(file.read())
    
# open_file()


# -------------------- working with JSON --------------------


from pathlib import Path
import json

characters = {
  'characters':[
    {"name": "Taiki", 'age':"17"},
    {"name": "Hata", 'age':"14"},
    {"name": "Senpay", 'age':"18"},
  ]
}

path = Path(__file__).parent / 'characters.json'

def write_json():
  with path.open("w") as file:
    json.dump(characters, file,indent=2)
    
def read_json():
  with path.open("r") as file:
    print(json.load(file))
read_json()