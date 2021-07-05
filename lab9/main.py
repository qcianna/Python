'''Proszę utworzyć klasę IFS (Iterated Function System), a w niej:
    - metodę inicjalizującą przyjmującą jako parametr współczynniki przekształcenia oraz prawdopodobieństwa 
    i określającą początkowe współrzędne punktu jako (0,0),
    - metodę dokonującą przekształcenia; jako parametr proszę przekazać liczbę iteracji. 
    W każdej iteracji przy obliczaniu nowych współrzędnych punktu należy wylosować z określonym prawdopodobieństwem 
    inną szóstkę z danego zestawu współczynników.
    Współrzędne obliczamy wg wzorów:
    x(t+1)=a*x(t)+b*y(t)+c
    y(t+1)=d*x(t)+e*y(t)+f
    - metodę rysującą otrzymany wynik'''
print("\n### ZAD1 ###\n")

import random
import matplotlib.pyplot as pl

class IFS:
  
  def __init__(self, przeksz, prawd):
    self._wspol = przeksz
    self._prawd = prawd
    self._x = [0]
    self._y = [0]

  def przeksztalc(self, n):
    for i in range(1, n):
      lista = random.choices(self._wspol, self._prawd)[0]
      a = lista[0]
      b = lista[1]
      c = lista[2]
      d = lista[3]
      e = lista[4]
      f = lista[5]

      (self._x).append(a*self._x[i-1] + b*self._y[i-1] + c)
      # print(self._x)
      (self._y).append(d*self._x[i-1] + e*self._y[i-1] + f)
      # print(self._y)
  
  def rysuj(self):
    pl.plot([i for i in self._x], [i for i in self._y], linestyle = '', marker = ',')
    pl.show()


# wsp = ((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035))
# pr = (0.90, 0.05, 0.05)
# r = IFS(wsp, pr)
# r.przeksztalc(100000)
# r.rysuj()

################
# wsp = ((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487))
# pr = [1 for _ in range(len(wsp))]
# r = IFS(wsp, pr)
# r.przeksztalc(100000)
# r.rysuj()

################
wsp = ((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795))
pr = (0.8, 0.2)
r = IFS(wsp, pr)
r.przeksztalc(100000)
r.rysuj()

'''Proszę utworzyć klasę Wektor, a w niej metody przeciążające operatory dodawania, odejmowania, mnożenia (mnożenie wektora przez liczbę) oraz metodę str. 
Proszę napisać także metody zwracające odpowiednio długość wektora, iloczyn skalarny, wektorowy i mieszany (proszę wykorzystać wcześniej zdefiniowane metody)'''
print("\n### ZAD2 ###\n")

import math

class Wektor:
  
  def __init__(self, x = 0, y = 0, z = 0):
    self._x = x
    self._y = y
    self._z = z

  def __str__(self):
    return ("Wektor: (" + str(self._x) + ", " + str(self._y) + ", " + str(self._z) + ")")

  def __add__(self, inny):
    w = Wektor()
    w._x = self._x + inny._x
    w._y = self._y + inny._y
    w._z = self._z + inny._z
    return w

  def __sub__(self, inny):
    w = Wektor()
    w._x = self._x - inny._x
    w._y = self._y - inny._y
    w._z = self._z - inny._z
    return w
  
  def __mul__(self, a):
    self._x *= a
    self._y *= a
    self._z *= a
    return self
  
  __rmul__ = __mul__

  def dlugosc(self):
    return math.sqrt(pow(self._x,2) + pow(self._y,2) + pow(self._z,2))

  def skalarny(self, inny):
    return self._x*inny._x + self._y*inny._y + self._z*inny._z

  def wektorowy(self, inny):
    w = Wektor()
    w._x = self._y*inny._z - self._z*inny._y
    w._y = - (self._x*inny._z - self._z*inny._x)
    w._z = self._x*inny._y - self._y*inny._x
    return w
  
  def mieszany(self, inny1, inny2):
    return self.skalarny(inny1.wektorowy(inny2))

w = Wektor(1,2,3)
print(w)
u = Wektor(1,1,2)
v = Wektor(0,3,4)
print("dlugosc = ", v.dlugosc())
print("skalarny = ", u.skalarny(v))
print("wektorowy = ", u.wektorowy(v))
print("mieszany = ", u.mieszany(v,w))
x = w + u
x = w - u
print(x)
z = 3 * x * 3
print(z)

'''Proszę utworzyć funkcje obliczające odpowiednio (parametry obiekty wcześniej utworzonej klasy):
    - strumień indukcji magnetycznej: Φ=B•S
    - siłę Lorentza F=q(E+v × B)
    - pracę siły Lorentza W=qE•v'''
print("\n### ZAD3 ###\n")

def indukcja(B, S):
  return B.skalarny(S)

def Lorentz(q,E,v,B):
  return q * (E + v.wektorowy(B))

def praca_sily(q,E,v):
  return q * (E.skalarny(v))


B = Wektor(1,1,1)
S = Wektor(2,1,3)
E = Wektor(1,2,1)
v = Wektor(1,0,1)
q = 1

print("strumien indukcji = ", indukcja(B,S))
print("sila Lorentza =", Lorentz(q,E,v,B))
print("praca sily Lorentza = ", praca_sily(q,E,v))