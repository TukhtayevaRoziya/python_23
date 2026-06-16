def read_file ():
  file = open("characters.txt",'r')
  # content=file.read()
  # print(content)
  # we need to close the file because of saving storage and preventing to get leaked
  lines = file.readlines()
  for line in lines:
    print(line)
    
  file.close()
  
  
  
read_file()
    