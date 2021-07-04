'''Proszę napisać trzy funkcje generatorowe:
    - zwracającą kolejną liczbę naturalną (nieskończony),
    - zwracającą te wartości z przekazanej jako parametr sekwencji, które są liczbami doskonałymi (liczby naturalne, która są sumą wszystkich swoich dzielników właściwych)
    - zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji                    
Korzystając ze zdefiniowanych funkcji proszę wypisać doskonałe liczby naturalne mniejsze od 10000'''
print("\n### ZAD1 ###\n")

def natural():
  i = 0
  while True:
    yield i
    i += 1

def perfect(l):
  for i in l:
    if sum(x for x in range(1,i) if i%x == 0) == i:
      yield i

def my_break(l, my_max):
  for i in l:
    if i > my_max:
      break
    yield i

print(list(perfect(my_break(natural(), 10000))))
print()

'''Proszę napisać generator obliczający ui wg zależności:
ui=ui-1+a/xi-1, z wartością początkową u0=0 dla x0=1 oraz z xi=x0+ia
Obliczenia proszę wykonać dla a=0.05 i przerwać je dla x=1.5. 
Zależność pozwala na wyznaczenie przybliżonej wartości logarytmu naturalnego z danej liczby. 
Generator ma zwracać x oraz przybliżoną i dokładną wartość logarytmu naturalnego '''
print("\n### ZAD2 ###\n")

import math

def calculate(a):
  u = 0
  x_0 = 1
  x = x_0
  i = 1
  while x < 1.5:
    u = u + a / x
    x = x_0 + i*a
    yield (x, u, math.log(x))
    i += 1

for i in calculate(0.05):
  print(i)
print()

'''Każdą liczbę całkowitą można zapisać jako sumę wartości całkowitych mniejszych od niej samej, 
np. 4 można zapisać jako: 1+1+1+1, 1+1+2, 1+3 oraz 2+2. 
Proszę napisać generator zwracający wszystkie możliwe sumy dla określonej wartości n '''
print("\n### ZAD3 ###\n")

#probably should be recursive XD

def gen(n):
  lista = [1 for i in range(n)]
  i = 0
  while len(lista) >= 1:
    yield lista
    lista[i] += lista[i+1]
    lista.pop()
    i = len(lista)-2
      
for i in gen(5):
  print(i)
print("\n")
    
'''Proszę napisać generator zwracający liczby spełniające warunek, 
że wartość kolejna jest co najmniej o 0.4 mniejsza lub większa od wartości poprzedniej. 
Działanie generatora należy zakończyć, jeżeli wylosowana wartość jest mniejsza od 0.1'''
print("\n### ZAD4 ###\n")

import random

def gen_rand():
  x1 = random.random()
  x2 = random.random()
  while x1 >= 0.1:
    if math.fabs(x1-x2) > 0.4:
      yield x1, x2
    x2 = x1
    x1 = random.random()

print(list(gen_rand()))

'''Proszę napisać generator działający dokładnie tak samo jak wbudowany range 
(proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych'''
print("\n### ZAD5 ###\n")

def my_range(start=0, stop=None, step=1):
  if stop == None and start <= 0:
    return
  elif stop == None and start > 0:
    stop, start = start, 0

  if start < stop and step < 0:
    return
  elif start > stop and step > 0:
    return
  
  if start < stop:
    while start < stop:
      yield start
      start += step
  else:
    while start > stop:
      yield start
      start += step


for i in range(8):
  print(i)
print("\n")
for i in range(-8):
  print(i)
print("\n")
for i in range(1,8):
  print(i)
print("\n")
for i in range(8,1):
  print(i)
print("\n")
for i in range(1,8,2):
  print(i)
print("\n")
for i in range(1,8,-2):
  print(i)
print("\n")
for i in range(8,1,2):
  print(i)
print("\n")
for i in range(8,1,-2):
  print(i)
print("\n")

for i in my_range(8):
  print(i)
print("\n")
for i in my_range(-8):
  print(i)
print("\n")
for i in my_range(1,8):
  print(i)
print("\n")
for i in my_range(8,1):
  print(i)
print("\n")
for i in my_range(1,8,2):
  print(i)
print("\n")
for i in my_range(1,8,-2):
  print(i)
print("\n")
for i in my_range(8,1,2):
  print(i)
print("\n")
for i in my_range(8,1,-2):
  print(i)
print("\n")
for i in my_range(1.5,8):
  print(i)