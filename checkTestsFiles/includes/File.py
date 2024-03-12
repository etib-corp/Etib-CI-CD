class File:
  def __init__(self, cwd : str, name : str):
    self.name = name
    self.cwd = cwd

  def isSame(self, other):
    return self.name == other.name