'''Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: 
pętla for, lista składana, funkcja map i wyrażenie generatorowe'''
print("\n### ZAD1 ###\n")

import time
import sys

m = 1000
N = 10000

def tester(func):
  for i in range(m):
    func(N)

def forStatement(n):
  my_list = []
  for i in range(n):
    my_list.append(i)
  suma = sum(range(n))


def listComprehension(n):
  my_list = [i for i in range(n)]

def mapFunction(n):
  my_list = map(lambda x: x, range(n))

def generatorExpression(n):
  my_list = (i for i in range(n))

print(sys.version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
  t1 = time.perf_counter()
  print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
  t2 = time.perf_counter()
  print("czas: ", t2-t1)


'''Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji filter
Koło o promieniu 1 wpisujemy w kwadrat o boku 2 i umieszczamy ich środki 
w początku układu współrzędnych. 
Stosunek pól tych figur jest równy stosunkowi liczby trafień w ich obszar, 
przy losowaniu dużej liczby punktów wewnątrz kwadratu.'''
print("\n### ZAD2 ###\n")

import math
import random

N = 10000

l = list(filter(lambda x: math.sqrt((random.uniform(-1,1)**2) + (random.uniform(-1,1)**2)) < 1, range(N)))

print(len(l)*4/N)

'''Proszę znaleźć:
    - największą wartość w każdym wierszu macierzy (map),
    - największą wartość w każdej kolumnie macierzy (map+zip)
Każde polecenie jedna linijka'''
print("\n### ZAD3 ###\n")

A = [[2, 3, 6, 1],
    [4, 2, 0, 8],
    [2, 7, 9, 1]]

ad_1 = list(map(max, A))
print(ad_1)

ad_2 = list(map(max, zip(*A)))
print(ad_2)

'''Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. 
Korzystając z funkcji wbudowanych reduce i map proszę obliczyć 
(i zwrócić z funkcji) 
wartości dofitowanych współczynników prostej oraz ich niepewności'''
print("\n### ZAD4 ###\n")

import functools

def fitting(x, y):
    x_avg = functools.reduce(lambda x1, x2: x1+x2, x)/len(x)
    D = functools.reduce(lambda x1, x2: x1 + x2, map(lambda x: (x-x_avg)**2, x))
    a = functools.reduce(lambda x1, x2: x1 + x2, map(lambda x, y: y*(x - x_avg),x,y))/D
    y_avg = functools.reduce(lambda x1, x2: x1+x2, y) / len(y)
    b = y_avg - a*x_avg
    dy = math.sqrt(functools.reduce(lambda x1, x2: x1+x2, map(lambda x,y: (y-(a*x+b))**2,x,y)))
    da = dy/math.sqrt(D)
    db=dy*math.sqrt(1/len(x) + x_avg**2/D)
    return a, b, da, db

print(fitting([1,2,3,4],[1,6,7,4]))
