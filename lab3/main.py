'''Proszę napisać funkcję, do której można przekazać zmienną liczbę parametrów, zwracającą listę. 
Do wynikowej listy trafiają elementy, które powtarzają się we wszystkich parametrach przekazanych do funkcji, 
np. ([1,2,3], (1,3,5), [3,2]) -> [3], ([1,2,3], (1,3,5), [3,2,1]) -> [1,3].
Proszę użyć konstrukcji for-else'''
print("\n### ZAD1 ###\n")

def func1(*l):
  my_list = []
  for i in l[0]:
    for j in l[1:]:
      if i not in j:
        break
    else: 
      my_list.append(i)
  return my_list

print(func1([1,2,3], (1,3,5), [3,2,1]))

'''Proszę napisać funkcję przyjmującą dwie sekwencje i parametr z wartością domyślną True. 
Funkcja zwraca listę dwuelementowych krotek zawierających elementy o tych samych indeksach z obu sekwencji. 
Jeżeli wartość trzeciego parametru wynosi True, długość zwracanej listy równa jest długości krótszej z przekazanych sekwencji, 
w przeciwnym wypadku brakujące elementy w krotkach uzupełniamy wartością None. 
Budowanie każdej z wynikowych list jedna linijka, proszę nie używać funkcji wbudowanych!'''
print("\n### ZAD2 ###\n")

def func2(x, y, check = True):
  my_list = []
  if check==True:
    my_list = [(x[i], y[i]) for i in range(len(x) if len(x)<len(y) else len(y))]
  else:
    my_list = [(x[i] if i < len(x) else None, y[i] if i < len(y) else None) for i in range(len(x) if len(x) > len(y) else len(y))]
  
  return my_list

print(func2([2,3,4],(1,2,3,5,7), False))

'''Proszę napisać funkcję umożliwiającą rozmienienie kwoty pieniędzy przekazanej jako jej pierwszy parametr 
nominałami określonymi poprzez drugi parametr - wartość domyślna krotka (10,5,2) (algorytm zachłanny). 
Proszę sprawdzić działanie funkcji przekazując inny zestaw monet'''
print("\n### ZAD3 ###\n")

def func3(amount, denom = (10, 5, 2)):
  res = {}

  for i in denom:
    counter = 0
    while i <= amount:
      amount -= i
      counter += 1
    res[i] = counter
  
  if amount != 0:
    print("It's not possible to change money")

  return res

print(func3(39,(5, 2, 1)))

'''Proszę napisać funkcję przyjmującą cztery parametry: liczba całkowita, 
której wartość zgadujemy, granice przedziału, w którym szukana liczba się mieści 
i ostatni określający sposób poszukiwania wartości z wartością domyślną 'r'. 
Przy wartości domyślnej ostatniego parametru, liczby poszukujemy losując kolejną wartość, 
w innym przypadku poszukujemy wartości poprzez podział przedziału poszukiwania wartości na pół. 
W obu przypadkach w każdym kroku odpowiednio zawężamy przedział poszukiwania (proszę wykorzystać operator trójargumentowy). 
Proszę sprawdzić ile kroków jest potrzebnych do znalezienia szukanej wartości w zależności od metody'''
print("\n### ZAD4 ###\n")

import random

def func4(magic_number, a1, a2, mode = 'r'):
  if mode == 'r':
    counter = 0
    guess = random.randint(a1, a2)
    while (guess != magic_number):
        print(guess)
        guess = random.randint(a1, a2)
        counter += 1
    print("counter: ", counter)
  else:
    counter = 0
    guess = random.randint(a1, a2)
    while (guess != magic_number):
        print(guess)
        guess = random.randint(a1, a2)
        middle = (a1 + a2) // 2
        a1 = middle if middle <= magic_number else a1
        a2 = middle if middle > magic_number else a2
        counter += 1
    print("counter: ", counter)

func4(2,0,10,'b')