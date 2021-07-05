import string

def zakoduj_cezar(name, l):
  zakodowany_text = ""
  print(string.ascii_letters)
  with open(name) as f:
    for c in f.read():
      if c in string.ascii_letters:
        nowa_pozycja = (ord(c) + l)
        while nowa_pozycja > ord('z'):
          nowa_pozycja -= 26
        # while nowa_pozycja < ord('A'):
        #   nowa_pozycja += 26
        zakodowany_text += chr(nowa_pozycja)
        # nowa_pozycja = (ord(c) + l) % len(string.ascii_lowercase)
        # zakodowany_text += string.ascii_lowercase[nowa_pozycja]
      else:
        zakodowany_text += c
  
  with open("zakodowany.txt", "w") as f2:
    f2.write(zakodowany_text)

  
def odkoduj_cezar(name, l):
  odkodowany_text = ""
  with open(name) as f:
    for c in f.read():
      if c in string.ascii_letters:
        nowa_pozycja = (ord(c) - l)
        while nowa_pozycja > ord('z'):
          nowa_pozycja -= 26
        # while nowa_pozycja < ord('A'):
        #   nowa_pozycja += 26
        odkodowany_text += chr(nowa_pozycja)
        pass
      else:
        odkodowany_text += c
  
  with open("odkodowany.txt", "w") as f2:
    f2.write(odkodowany_text)


