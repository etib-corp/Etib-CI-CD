import os
from colorama import Fore, Back

from src.Parser import getFiles
from src.Display import printDir

def Help():
  with open('man.txt') as file:
    lines = file.readlines()
    for line in lines:
      print(Fore.BLUE + line)

def TestFileChecker(flags : dict):
  if flags["help"]:
    return Help()
  cwd = os.getcwd()

  if os.path.exists(cwd + '/tests') == False:
    print(Back.RED + "STRUCTURE ERROR:" + Back.RESET + Fore.RED + " Test directory does not exist.")
    return -1
  src = getFiles(cwd, '/src')
  tests = getFiles(cwd, '/tests')

  if flags["display"]:
    print(Fore.MAGENTA)
    printDir(tests, 0)
    print("\n\n")
    print(Fore.CYAN)
    printDir(src, 0)
  if src.compareTo(tests, True):
    print(Back.GREEN + "OK:" + Back.RESET + Fore.GREEN + " All test files exists.")
  else:
    print(Back.YELLOW + "WARNING:" + Back.RESET + Fore.YELLOW + " Some tests are missing OR there are too many tests files compared to source code.")
    return -1
  return 0