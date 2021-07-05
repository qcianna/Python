'''Proszę utworzyć funkcję sprawdzającą poprawność numeru PESEL
Parametrami wejściowymi do funkcji są: 
Pesel, data urodzenia (datetime.date) oraz płeć
    cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
    cyfry 3-4 to dwie cyfry miesiąca urodzenia
    cyfry 5-6 to dwie cyfry dnia urodzenia
    cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
    cyfra 11 suma kontrolna
Do numeru miesiąca dodawane są następujące wartości w zależności od roku:
    dla lat 1800 - 1899 - 80
    dla lat 1900 - 1999 - 0
    dla lat 2000 - 2099 - 20
    dla lat 2100 - 2199 - 40
    dla lat 2200 - 2299 - 60'''
print("\n### ZAD1 ###\n")

import datetime

def check_pesel(pesel, data, plec):

  if len(pesel) != 11:
    raise Exception("zly rozmiar peselu")

  tab_pesel = []
  for i in pesel:
    tab_pesel.append(int(i))
  wagi = [1,3,7,9,1,3,7,9,1,3]
  suma_kontrolna = 0
  for i in range(len(wagi)):
    suma_kontrolna = tab_pesel[i]*wagi[i]
    suma_kontrolna = suma_kontrolna % 10
    suma_kontrolna = 10 - suma_kontrolna
    suma_kontrolna = suma_kontrolna % 10
  if suma_kontrolna != tab_pesel[len(tab_pesel)-1]:
    raise Exception("zla suma kontrolna")

  if (tab_pesel[9] % 2 and plec == "kobieta") or (tab_pesel[9] % 2 == 0 and plec == "mezczyzna"):
    raise Exception("zla plec")

  dzien = tab_pesel[4]*10 + tab_pesel[5]
  if dzien != data.day:
    raise Exception("zly dzien")
  
  if data.year < 2000 and data.year > 1900:
    rok = 1900
    miesiac = 10*tab_pesel[2] + tab_pesel[3]
  else:
    rok = 2000
    miesiac = 10*tab_pesel[2] + tab_pesel[3] - 20
  rok += 10*tab_pesel[0] + tab_pesel[1]
  if rok != data.year:
    raise Exception("zly rok")

  if miesiac != data.month:
    raise Exception("zly miesiac")

  print("dobry pesel")


print("1")
p = "02071803624"
d = datetime.date(1902,7,8)
km = "kobieta"

try:
  check_pesel(p,d,km)
except Exception as err:
  print(err)

print("2")
p2 = "02270803624"
d2 = datetime.date(2002,7,8)
km2 = "kobieta"

try:
  check_pesel(p2,d2,km2)
except Exception as err:
  print(err)

print("3")
p2 = "02270803624"
d2 = datetime.date(2002,7,8)
km2 = "mezczyzna"

try:
  check_pesel(p2,d2,km2)
except Exception as err:
  print(err)
  print()

'''Proszę napisać funkcję zwracającą średni wiek osób, który daty urodzenia zapisane są w plik daty.in.
Funkcja powinna móc działać w trybie 'restrykcyjnym' - po napotkaniu niepoprawnej daty/wpisu 
zgłoszenie wyjątku i zakończenie działania, w trybie 'liberalnym' - niepoprawne wpisy są ignorowane.
Linia w pliku jest poprawna, jeśli zawiera dzień, miesiąc i rok,  
które tworzą poprawną datę - zgodność liczby dni w miesiącu, 
w tym odpowiednia długość lutego w zależności od tego czy rok jest przestępny czy nie.
Rok przestępny: podzielny przez 4 i niepodzielny przez 100 lub podzielny przez 400'''
print("\n### ZAD2 ###\n")

def wez_srednia(name):
  with open(name) as f:
    data = f.readlines()
    if not data:
      raise Exception("plik pusty")
    daty = []
    for i in data:
      daty.append(i.split())

    for i in daty:
      dni_miesiace = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      for j in range(len(i)):
        i[j] = int(i[j])

      if len(i) < 3:
        raise Exception("za malo danych")
      if (i[2]%4==0 and i[2]%100) or (i[2]%400==0):
        dni_miesiace[1] = 29
      if (i[1] < 1 or i[1] > 12):
        raise Exception("zly miesiac")
      if (i[0] < 1 or i[0] > dni_miesiace[i[1]]):
        raise Exception("zly dzien")
  
  srednia = sum()
  return srednia

try:
  print(wez_srednia("daty.in"))
except Exception as err:
  print(err)

'''Proszę napisać funkcję sprawdzającą czy elementy listy tworzą trójkę (a2+b2=c2)/czwórkę(a2+b2+c2=d2) pitagorejską (funkcja ma działać dla dowolnej długości "podciągu"!). 
Proszę zgłosić wyjątek w przypadku niepoprawnej długości listy oraz w przypadku, 
gdy lista nie zawiera żadnych trójek/czwórek pitagorejskich. Dla każdej trójki/czwórki proszę sprawdzić ile jest w niej wartości parzystych i nieparzystych'''
print("\n### ZAD3 ###\n")

def pit(lista, n):
  if n!=3 and n!=4:
    raise Exception("podany parametr jest zly (ma byc 3 lub 4)")
  if len(lista) < n:
    raise Exception("rozmiar listy jest nieprawidlowy")
  for i in range(0, len(lista)-n, n):
    
    licznik = 0

    parzyste = 0
    for j in range(i, i+n):
      if lista[j] % 2 == 0:
        parzyste += 1
      
    if sum(x**2 for x in lista[i:(i+n-1)]) == lista[i+n-1]**2:
      licznik += 1
      print(str(lista[i:(i+n)]) + ": parzyste = " + str(parzyste) + " nieparzyste  = " + str(n-parzyste))

    if licznik == 0:
      raise Exception("nie znaleniono " + str(n) + " pitagorejskiej w liscie")

l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)

try:
  pit(l, 3)
except Exception as err:
  print(err)

l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)

try:
  pit(l, 4)
except Exception as err:
  print(err)

l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)

try:
  pit(l, 3)
except Exception as err:
  print(err)

l=(1,2,3,4,5,6,7,8,9)

try:
  pit(l, 3)
except Exception as err:
  print(err)


