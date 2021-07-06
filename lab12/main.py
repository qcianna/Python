'''Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie. 
Obie współrzędne proszę zdefiniować jako własności (metoda inicjalizacyjna bezparametrowa)'''
print("\n### ZAD1 ###\n")

class Punkt:

  def __init__(self):
    self.x = 0
    self.y = 0
  
  @property
  def x(self):
    # print("x.prop")
    return self._x
  
  @property
  def y(self):
    return self._y

  @x.setter
  def x(self, val):
    # print("x.set")
    self._x = val

  @y.setter
  def y(self, val):
    self._y = val

  @x.getter
  def x(self):
    # print("x.get")
    return self._x
  
  @y.getter
  def y(self):
    return self._y

p = Punkt()
print(p.x, p.y)
p.x = 1
p.y = 2
print(p.x, p.y)

'''Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem (implementowanym jako funkcja) 
sprawdzającym czy współrzędne leżą w określonym zakresie, jeżeli nie - proszę zgłosić wyjątek'''
print("\n### ZAD2 ###\n")

def sprawdz_zakres(a, b):
  def fz(pf):
    # print("zewnetrzna", pf.__name__)
    def fw(p1, p2):
      # print("wewnetrzna", p1, p2)
      # print(p1.x, p1.y, " ", p2.x, p2.y)
      if a <= p1.x and p1.x <= b and a <= p1.y and p1.y <= b and a <= p2.x and p2.x <= b and a <= p2.y and p2.y <= b:
        return pf(p1, p2)
      else:
        raise Exception("zły zakres")
      # print("koniec wew")
    return fw
    # print("koniec zew")
  return fz

@sprawdz_zakres(-5, 5)
def dodaj(p1, p2):
  suma = Punkt()
  suma.x = p1.x + p2.x
  suma.y = p1.y + p2.y
  return suma

@sprawdz_zakres(-5, 5)
def odejmij(p1, p2):
  roznica = Punkt()
  roznica.x = p1.x - p2.x
  roznica.y = p1.y - p2.y
  return roznica

p1 = Punkt()
p1.x = 5
p1.y = 4

p2 = Punkt()
p2.x = 1
p2.y = 2

try:
  p_suma = dodaj(p1, p2)
  print("suma: ", p_suma.x, p_suma.y)
  p_roznica = odejmij(p1, p2)
  print("roznica: ", p_roznica.x, p_roznica.y)
except Exception as err:
  print(err)
print()

p2 = Punkt()
p2.x = 1
p2.y = 8

try:
  p_suma = dodaj(p1, p2)
  print("suma: ", p_suma.x, p_suma.y)
  p_roznica = odejmij(p1, p2)
  print("roznica: ", p_roznica.x, p_roznica.y)
except Exception as err:
  print(err)

'''Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta 
(dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1)
Wzór Herona: P=[p(p-a)(p-b)(p-c)]1/2, gdzie: a,b,c - długości boków, p - połowa obwodu
Wzór Brahmagupty: P=[(p-a)(p-b)(p-c)(p-d)]1/2, oznaczenia j.w.'''
print("\n### ZAD3 ###\n")

import math

class Oblicz:

  @staticmethod
  def Trojkat(A, B, C):

    a = math.sqrt(pow((B.x - A.x),2) + pow(B.y - A.y,2))
    b = math.sqrt(pow((C.x - B.x),2) + pow(C.y - B.y,2))
    c = math.sqrt(pow((C.x - A.x),2) + pow(C.y - A.y,2))

    obwod = a + b + c

    p = obwod/2
    pole = (p*(p - a)*(p - b)*(p - c))**0.5

    return "obwod: " + str(obwod) + "\npole: " + str(pole)
  
  @staticmethod
  def Czworokat(A, B, C, D):

    a = math.sqrt(pow((B.x - A.x),2) + pow(B.y - A.y,2))
    b = math.sqrt(pow((C.x - B.x),2) + pow(C.y - B.y,2))
    c = math.sqrt(pow((D.x - C.x),2) + pow(D.y - C.y,2))
    d = math.sqrt(pow(D.x - A.x,2) + pow(D.y - A.y,2))

    obwod = a + b + c + d

    p = obwod/2
    pole = ((p - a)*(p - b)*(p - c)*(p - d))**0.5

    return "obwod: " + str(obwod) + "\npole: " + str(pole)

#wierzcholki
A = Punkt()

B = Punkt()
B.x = 4
B.y = 0

C = Punkt()
C.x = 4
C.y = 4

D = Punkt()
D.x = 0
D.y = 4

print(Oblicz.Trojkat(A, B, C))
print()
print(Oblicz.Czworokat(A, B, C, D))
print()

# print(Oblicz.obwod(A, B, C))
# print()

'''Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby wywołań poszczególnych funkcji obłożonych dekoratorem, 
z metodą statyczną zwracającą wynik'''
print("\n### ZAD3 ###\n")

class Dec:

  licznik = 0
  wywolania = {}

  def __init__(self, pf):
    self.pf = pf
    Dec.wywolania[self.pf] = 0

  def __call__(self, *p):
    Dec.licznik += 1
    Dec.wywolania[self.pf] += 1
    return self.pf(*p)
  
  @staticmethod
  def print():
    print("wszystkie wywolania: ", Dec.licznik)
    for nazwa, ilosc in Dec.wywolania.items():
      print(nazwa.__name__, ":", ilosc)

@Dec
def fsum(p):
  return sum(p)

@Dec
def f():
  pass
  
fsum(range(10))
fsum(range(10))
fsum(range(10))

f()
f()

Dec.print()