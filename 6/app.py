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

from pathlib import Path

def create_path():
  script_dir = Path(__file__).parent
  path = script_dir / 'characters'
  path.mkdir(parents=True, exist_ok=True)
create_path()
