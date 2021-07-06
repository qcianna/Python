'''Proszę napisać abstrakcyjną klasę Calka z metodą inicjalizacyjną określającą granice całkowania, liczbę kroków oraz funkcję podcałkową 
(proszę skontrolować poprawność przekazanych parametrów) oraz metodą abstrakcyjną obliczającą wartość całki.
Następnie proszę utworzyć klasy dziedziczące po klasie Calka z metodami obliczającymi wartość całki odpowiednio metodą trapezów lub Simpsona, 
w metodzie proszę umieścić komentarz dokumentacyjny.'''
print("\n### ZAD1 ###\n")

import abc
import inspect
import math

class Calka(abc.ABC):

  def __init__(self, a, b, n, f):
    if n <= 0:
      raise Exception("zła liczba krokow")
    if inspect.isfunction(f) == False:
      raise Exception("zły parametr - nie funkcja")
    self.a = min(a,b)
    self.b = max(a,b)
    self.n = n
    self.f = f
  
  @abc.abstractclassmethod
  def calkowanie(self):
    '''Metoda abstrakcyjna'''


class MetodaTrapezow(Calka):

  def calkowanie(self):
    '''Definicja metody abstrakcyjnej - trapezy'''
    h = (self.b - self.a)/self.n
    suma = 0
    for i in range(self.n):
      suma += self.f(self.a + i*h) + self.f(self.a + h*(i+1))
    return suma*(h/2)

class MetodaSimpsona(Calka):

  def calkowanie(self):
    '''Definicja metody abstrakcyjnej - Simpson'''
    h = (self.b - self.a)/(2*self.n)
    suma = self.f(self.a)
    for i in range(1, 2*self.n):
      if i%2:
        suma += 4*self.f(self.a+i*h)
      elif i%2 == 0:
        suma += 2*self.f(self.a+i*h)
    suma += self.f(self.a+2*self.n*h)
    return (h/3)*suma

try:
  print(MetodaTrapezow(0,math.pi/2,10,lambda x: math.sin(x)).calkowanie())
  print(MetodaSimpsona(0,math.pi/2,10,lambda x: math.sin(x)).calkowanie())
except Exception as err:
  print(err)
print()

'''Proszę napisać klasę implementującą stos, klasa ma obsługiwać możliwość tworzenia pustego stosu bądź inicjalizacji istniejącym stosem (obiektem klasy), 
dodawania i usuwania elementu, dodawania elementów innego stosu, zwracania rozmiaru i wypisywania stosu.
Następnie proszę napisać klasę dziedziczącą po klasie stosu i implementującą stos posortowany (rosnąco lub malejąco). 
W tym przypadku element/elementy innego stosu można do stosu dodać pod warunkiem zachowania porządku sortowania.
Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100] 
losując 100 wartości (średnia po 100 powtórzeniach)'''
print("\n### ZAD2 ###\n")

import random

class Stos:

  def __init__(self, stos = None):
    if stos is not None:
      self.elementy = stos.elementy[:]
    else:
      self.elementy = []
  
  def add(self, el):
    self.elementy.append(el)
  
  def delete(self):
    self.elementy.pop()
  
  def add_other(self, stos):
    self.elementy.extend(stos.elementy)
  
  def len(self):
    return len(self.elementy)
  
  def print(self):
    for i in range(len(self.elementy)):
      print(self.elementy[i], end = ', ')
    print()

stos = Stos()
stos.add(4)
stos.add(7)
stos.add(4)
stos.print()
stos.delete()
stos2 = Stos(stos)
stos2.add(1)
stos2.add_other(stos)
stos2.print()
print(stos2.len())
print()

class StosPosortowany(Stos):
  
  def add(self, el):
    if self.len() == 0 or el >= self.elementy[-1]:
      self.elementy.append(el)

  def add_other(self, stos):
    if self.len() == 0 or stos.elementy[0] >= self.elementy[-1]:
      self.elementy.extend(stos.elementy)

stos = StosPosortowany()
stos.add(8)
stos.add(13)
stos.add(4)
stos.print()
stos2 = StosPosortowany(stos)
stos2.add(1)
stos2.add(15)
stos2.add_other(stos)
stos2.print()
print(stos2.len())

suma = 0 
for i in range(100):
  s = StosPosortowany()
  for i in range(100):
    s.add(random.randint(0,100))
  suma += s.len()
print("średni rozmiar: ", suma/100)
print()

'''Proszę zaimplementować klasę pozwalającą na zliczanie linii, słów i znaków w pliku (metody inicjalizująca i zliczająca). 
W klasie proszę także zaimplementować bezparametrową metodę statyczną zwracają komunikat analogiczny do komunikatu zwracanego przez polecenie systemowe linuxa wc 
w przypadku jednoczesnego zliczania dla kilku plików
Przykład:
$wc AA.py BB.py
   50    91   944 AA.py
   80  117 1281 BB.py
 130  208 2225 razem'''
print("\n### ZAD3 ###\n")

class Licznik:

  wszystkie_linie = 0
  wszystkie_slowa = 0
  wszystkie_znaki = 0

  def __init__(self):
    self.linie = 0
    self.slowa = 0
    self.znaki = 0
  
  def zlicz(self, *nazwy_plikow):

    for pl in nazwy_plikow:
      with open(pl) as p:
        self.linie = 0
        self.slowa = 0
        self.znaki = 0
        for linia in p:
          self.linie += 1
          lista_slow = linia.split(" ")
          self.slowa += len(lista_slow)
          self.znaki += len(linia)
        print(self.linie, " ", self.slowa, " ", self.znaki, " ", pl)
        Licznik.wszystkie_linie += self.linie
        Licznik.wszystkie_slowa += self.slowa
        Licznik.wszystkie_znaki += self.znaki
    
    if (len(nazwy_plikow) > 0):
      Licznik.my_wc()

  @staticmethod
  def my_wc():
    print(Licznik.wszystkie_linie, " ", Licznik.wszystkie_slowa, " ", Licznik.wszystkie_znaki, "razem")

l = Licznik()
l.zlicz("text1.txt", "text2.txt")