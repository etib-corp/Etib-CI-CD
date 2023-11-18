import os
from includes.Directory import Directory
from includes.File import File

def getFiles(cwd, name):
  dir = Directory(cwd + "/" + name, name)
  listdir = os.listdir(dir.cwd)

  for element in listdir:
    newCwd = dir.cwd + '/' + element
    if os.path.isfile(newCwd):
      dir.appendFile(File(newCwd, element))
    elif os.path.isdir(newCwd):
      dir.appendDirectory(getFiles(dir.cwd, element))
    else:
      dir.appendFile(File(newCwd, element))

  return dir