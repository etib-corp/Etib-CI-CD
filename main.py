from src.TestFileChecker import TestFileChecker
import sys
from colorama import Fore, Back

def fillFlags(args):
  flags = {
    "display": False,
    "help": False,
    "report": False,
  }
  for arg in args:
    match arg:
      case "-h":
        flags["help"] = True
      case "--help":
        flags["help"] = True
      case "-d":
        flags["display"] = True
      case "--display":
        flags["display"] = True
      case "-r":
        flags["report"] = True
      case "--report":
        flags["report"] = True
      case _:
        print(Back.RED + "ARGUMENT ERROR:" + Back.RESET + Fore.RED + " Invalid Flag.")
        return None

  if (flags["display"] and flags["help"]) or (flags["report"] and flags["help"]):
    print(Back.RED + "ARGUMENT ERROR:" + Back.RESET + Fore.RED + " Incompatible Flag use.")
    return None
  return flags

def execute():
  args = sys.argv[1:]
  flags = fillFlags(args)

  print(Fore.RESET)
  print(Back.RESET)
  if flags is None:
    exit(-1)
  return TestFileChecker(flags)

execute()