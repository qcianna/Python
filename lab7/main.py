import mod1
import mod2
import mod3

# if __name__ == '__main__':
#   help(mod1)

'''Proszę utworzyć moduł a w nim:'''

print("\n### ZAD1 ###\n")
'''funkcję tworzącą trójkąt Pascala, do rzędu n'''
mod1.pascal(5)
print()

print("\n### ZAD2 ###\n")
'''funkcję tworzącą trójkąt Eulera, do rzędu n'''
mod2.euler(5)
print()

print("\n### ZAD3 ###\n")
'''funkcję kodującą plik szyfrem Cezara'''
liczba = 3
mod3.zakoduj_cezar("tekstPL.txt", liczba)

print("\n### ZAD4 ###\n")
'''funkcję dekodującą plik zakodowany szyfrem Cezara, wynik proszę zapisać do pliku'''
mod3.odkoduj_cezar("zakodowany.txt", liczba)