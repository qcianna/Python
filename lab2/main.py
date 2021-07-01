'''Proszę utworzyć k-elementową listę całkowitych wartości losowych z przedziału [0,5k).
Proszę sprawdzić ile elementów pozostaje na swoim miejscu po losowym przemieszaniu listy, 
mieszanie proszę wykonać 100 razy a wyniki zapisywać w słowniku'''
print('\n### ZAD1 ###\n')

import random

k = int(input("Give number: "))

l = [random.randrange(0, 5*k) for i in range(k)]
print(l)

l_cpy = l[:]
dic = {}
for i in range(100):
  counter = 0
  random.shuffle(l)
  for j in range(k):
    if l_cpy[j] == l[j]:
      counter += 1
  dic.setdefault(i, counter)
print(dic)

'''Proszę utworzyć losowy string o długości k zawierający tylko małe litery, 
pomiędzy poszczególne litery proszę wstawić kropkę'''
print('\n### ZAD2 ###\n')

import string 

my_string = '.'.join(random.choices(string.ascii_lowercase, k = k))
print(my_string)

'''Proszę utworzyć listę stu wartości losowych z przedziału [0,20). 
Następnie na jej podstawie proszę utworzyć słownik, w którym klucze są liczbami z listy, 
a wartościami lista ich indeksów.
     - w rozwiązaniu proszę wykorzystać metodę setdefault i funkcjię enumerate
     - w rozwiązaniu proszę wykorzystać metody setdefault i index'''
print('\n### ZAD3 ###\n')

l = [random.randrange(0,20) for i in range(100)]
print(l)
print()

dic = {}
for i, w in enumerate(l):
  dic.setdefault(w, []).append(i)
print(dic)
print()

for i in l:
  if l.index(i) not in dic[i]:
    dic.setdefault(i, []).append(l.index(i))
print(dic)

'''Proszę sprawdzić ile spośród 1000 losowych wartości całkowitych składających się z n cyfr, 
gdzie n jest z przedziału [3,6], jest liczbami palindromowymi. 
Wynik proszę zapisać w słowniku'''
print('\n### ZAD4 ###\n')

licznik = {f'liczba {i} cyfrowa' : 0 for i in range(3,7)}
for i in range(1000):
    r = random.randint(100, 999)
    if str(r) == str(r)[::-1]:
        licznik[f'liczba {3} cyfrowa'] += 1
    r = random.randint(1000, 9999)
    if str(r) == str(r)[::-1]:
        licznik[f'liczba {4} cyfrowa'] += 1
    r = random.randint(10000, 99999)
    if str(r) == str(r)[::-1]:
        licznik[f'liczba {5} cyfrowa'] += 1
    r = random.randint(100000, 999999)
    if str(r) == str(r)[::-1]:
        licznik[f'liczba {6} cyfrowa'] += 1

print(licznik)

'''Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne liczby naturalne, a wartościami liczby losowe z przedziału [1,100). 
Następnie w obu słownikach proszę zamienić miejscami klucze z wartościami.
Na podstawie tak otrzymanych słowników proszę utworzyć nowy słownik, 
w którym klucze są kluczami występującymi jednocześnie w obu wcześniej utworzonych słownikach, 
wartościami natomiast są dwuelementowe krotki wartości związanych z danym kluczem w słownikach oryginalnych'''
print('\n### ZAD5 ###\n')

def rev_dic(a):
   b = {}
   for key in a:
       b[a.get(key)] = b.get(a.get(key), []) + [key]
   return(b)

dic1 = {i: random.randrange(1, 100) for i in range(10)}
dic2 = {i: random.randrange(1, 100) for i in range(10)}
 
dic1 = rev_dic(dic1)
dic2 = rev_dic(dic2)
print(dic1)
print(dic2)

dic3 = {i : (dic1[i], dic2[i]) for i in dic1 if i in dic2}
print(dic3)