'''Proszę napisać iterator zwracający kolejne wyrazy ciągu Fibonacciego dwoma sposobami i porównać ich wykorzystanie'''
print("\n### ZAD1 ###\n")

class Fib1:

  def __init__(self, n):
    self.n = n
    self.a = 0
    self.b = 1

  def __iter__(self):
    return self
  
  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > self.n:
      raise StopIteration
    return self.a

class Fib2:

  def __init__(self, n):
    self.n = n
    self.a = 0
    self.b = 1

  def __iter__(self):
    return Fib2(self.n)

  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > self.n:
      raise StopIteration
    return self.a

  
print("\njedna klasa:")
f = Fib1(15)
for i in f:
  for i in f:
    print(i, end = " ")
  print()

print("\ndwie klasy:")
f = Fib2(15)
for i in f:
  for i in f:
    print(i, end = " ")
  print()

print("\n")

'''Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru:Xn+1 = (aXn + c) mod m, dla m = 231-1, a = 75, c = 0, x0 = 1.
Korzystając z zaimplementowanego iteratora proszę wylosować 105 par liczb z przedziału [0,1). 
Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n∈[1,10]. 
Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python'''
print("\n### ZAD2 ###\n")

import math
import random

class Pseudolos:

  def __init__(self):
    self.m = pow(2, 31) - 1
    self.a = pow(7, 5)
    self.c = 0
    self.x = 1

  def __iter__(self):
    return self
  
  def __next__(self):
    temp = self.x
    self.x = ((self.a * temp + self.c) % self.m)
    return self.x  / self.m

def calculate(l):
  for i in range(1, 11):
    wszystko = 0
    kwadrat = 0
    for x,y in l:
      wszystko += 1
      if (x <= 0.1*i and y <= 0.1*i):
        kwadrat += 1
    print(i, "-", kwadrat/wszystko * 100)
  print()

r = Pseudolos()
mojelosowe = [(next(r), next(r)) for _ in range(10**5)]
calculate(mojelosowe)

losowe = [(random.random(), random.random()) for _ in range(10**5)]
calculate(losowe)
print()

'''Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: 
xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej, 
np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10-5 (pochodna - scipy.misc)'''
print("\n### ZAD3 ###\n")

import scipy.misc

# def f(x):
#   return math.sin(x) - pow(0.5*x, 2)

def f(x):
  return x**2

class Newton_Raphson:

  def __init__(self, x, eps):
    self.x = x
    self.eps = eps

  def __iter__(self):
    return self

  def __next__(self):
    temp = self.x
    self.x = temp - f(temp)/scipy.misc.derivative(f, temp)
    if math.fabs(self.x - temp) < self.eps:
      raise StopIteration
    return self.x


x = 1.5
eps = 10e-5

n = Newton_Raphson(x, eps)
for i in n:
  print(i)
