import os
from src.Parser import getFiles
from src.Display import printDir

def TestFileChecker():
  cwd = os.getcwd()

  if os.path.exists(cwd + '/tests') == False:
    print('Test directory does not exist.')
    return -1
  src = getFiles(cwd, '/src')
  tests = getFiles(cwd, '/tests')

  printDir(tests, 0)
  print("\n\n")
  printDir(src, 0)
  if src.compareTo(tests, True):
    print("OK: All test files exists.")
  else:
    print("WARNING: Some tests are missing OR there are too many tests files compared to source code.")
    return -1
  return 0