'''Proszę utworzyć string składający się z elementów listy argv z wyłączeniem nazwy programu. 
Jeżeli program został uruchomiony bez podania parametrów proszę wypisać na ekran komunikat 
informujący o niewłaściwym sposobie uruchomienia programu'''
print("\n### ZAD1 ###\n")

import sys

if len(sys.argv) < 2:
    print("ERROR: Too few parameters")
    quit()
else:
    my_string = ''.join(sys.argv[1:])
    print(my_string)

'''Na podstawie wcześniej utworzonego stringa proszę utworzyć cztery listy: 
zawierającą małe litery, zawierającą duże litery, 
zawierającą cyfry oraz zawierającą wszystko co nie jest literą'''
print("\n### ZAD2 ###\n")

small_letters = []
big_letters = []
numbers = []
other = []

for i in my_string:
    if i.islower():
        small_letters.append(i)
    elif i.isupper():
        big_letters.append(i)
    elif i.isdecimal():
        numbers.append(int(i))
    else:
        other.append(i)

print(small_letters)
print(big_letters)
print(numbers)
print(other)

'''Na podstawie utworzonej listy zawierającej małe litery proszę utworzyć listę małych liter bez powtórzeń. 
Następnie proszę utworzyć nową listę, w której każdy element jest dwuelementową krotką 
(litera, krotność jej wystąpienia w liście oryginalnej)'''
print("\n### ZAD3 ###\n")

small_list = [small_letters[i] for i in range(len(small_letters)) if small_letters[i] not in small_letters[:i]]
print(small_list)

new_list = [(small_letters[i], small_letters.count(small_letters[i])) for i in range(len(small_letters)) if small_letters[i] not in small_letters[:i]]
print(new_list)

'''Otrzymaną w powyższym punkcie listę proszę wyświetlić w kolejności od najwyższej krotności'''
print("\n### ZAD4 ###\n")

new_list.sort(key = lambda x: x[1], reverse = True)
print(new_list)

'''Proszę utworzyć listę dwuelementowych krotek, w których pierwszy element jest liczbą pobraną z listy cyfr, 
drugi natomiast wartością funkcji liniowej ax+b dla danej liczby; 
wartości współczynników proszę ustalić w następujący sposób: 
a równa się liczbie samogłosek w stringu z punktu pierwszego, a b - liczbie spółgłosek tamże'''
print("\n### ZAD5 ###\n")

a = 0
for i in 'aeiouy':
  a += my_string.count(i)
  a += my_string.count(i.upper())
print(a)

b = len(my_string) - a - len(numbers) - len(other)
print(b)

y = [a*x+b for x in numbers]
next_list = [(numbers[i], y[i]) for i in range(len(numbers))]
print(next_list)

'''Proszę obliczyć wartości parametrów prostej korzystając z metody najmniejszych kwadratów'''
print("\n### ZAD6 ###\n")

x_avg = sum(numbers)/len(numbers)

D = sum([(x-x_avg)**2 for x in numbers])

a = 1/D*sum([y*(x-x_avg) for x,y in next_list])
print(a)

y_avg = sum(y)/len(y)

b = y_avg - a*x_avg
print(b)