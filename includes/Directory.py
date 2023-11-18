from File import File

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