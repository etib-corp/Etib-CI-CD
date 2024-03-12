from includes.File import File

class Directory:
  def __init__(self, cwd : str, name : str):
    self.cwd = cwd
    self.name = name
    self.directories = []
    self.files = []

  def appendDirectory(self, directory : object):
    self.directories.append(directory)

  def appendFile(self, file : File):
    self.files.append(file)

  def decompose(self):
    tab = []
    if len(self.directories) > 0:
      for directory in self.directories:
        tab.append(directory.decompose())
    for file in self.files:
      tab.append(file.name)
    tab.append(self.name)
    return tab

  def compareFiles(self, other):
    if len(other.files) != len(self.files):
      return False
    for fileToCompare in other.files:
      valid = False
      for fileReference in self.files:
        if fileReference.isSame(fileToCompare):
          valid = True
      if valid == False:
        return False
    return True

  def compareDirectories(self, other):
    if len(other.directories) != len(self.directories):
      return False
    for dirToCompare in other.directories:
      valid = False
      for dirReference in self.directories:
        if dirReference.compareTo(dirToCompare, False):
          valid = True
      if valid == False:
        return False
    return True

  def compareTo(self, other, isFirst):
    if not self.compareFiles(other):
      return False
    if self.name != other.name and not isFirst:
      return False
    return self.compareDirectories(other)
