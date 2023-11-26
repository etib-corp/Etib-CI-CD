from includes.Directory import Directory

def setSpace(space):
  if space > 0:
    print('|  ', end="")
  for i in range(space - 1):
    print("   ", end="")
  if space > 0:
    print('-->', end="")

def printFiles(files : list, space : int):
  for element in files:
    setSpace(space + 1)
    print(element.name)

def printDir(dir : Directory, range : int):
  setSpace(range)
  print(f"Name: {dir.name}")
  setSpace(range)
  print("Files:")
  printFiles(dir.files, range)
  if len(dir.directories) > 0:
    setSpace(range)
    print("Directories:")
    for directory in dir.directories:
      printDir(directory, range + 1)
  if range > 1:
    print("|")