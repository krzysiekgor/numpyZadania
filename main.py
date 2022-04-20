import random
import string

import numpy as np

# #zadanie 1
# tab=np.arange(3,3*16,3)
# print(tab)

#zadanie 2
# lista=np.arange(1,10,1,dtype='float64')
# print(lista)
# lista2 = lista.astype('int32')
# print(lista2)

# #zadanie 3
# def zwrocTablice(liczba):
#     lista = np.arange(1,(liczba*liczba)+1,1)
#     return lista.reshape(liczba,liczba)
# print(zwrocTablice(5))

#zadanie 4
# def zwrocPotegi(liczba,wykladnik):
#     return np.logspace(1,wykladnik+1,wykladnik,False,liczba,dtype='int32')
# print(zwrocPotegi(3,3))

#zadanie 5
# def generujMacierz(liczba):
#     wektor = np.array([x for x in range(liczba,0,-1)])
#     return np.diag(wektor)
# print(generujMacierz(5))

#zadanie 6
# def LosowaLitera(i):
#     return random.choices(string.ascii_uppercase, k=i)
# n=5
# poziomo='ROBOT'
# row = np.array(list(poziomo))
# #print(row)
# pionowo='KOT'
# col=np.array(list(pionowo))
#
# skos='SOK'
# diag=np.array(list(skos))
# macierz = np.array(LosowaLitera(n*n)).reshape([n,n])
# macierz[1] = row
# macierz[:3,3] = np.flip(col)
# np.fill_diagonal(macierz,diag)
# print(macierz)

#zadanie 7
# def wielokrotnosci(liczba):
#     linia = np.array([x for x in np.arange(2,liczba*2+2,2)])
#     wynik = np.zeros([liczba,liczba],dtype='int32')
#     for i in range(0,liczba,1):
#         wynik[i]=np.roll(linia,i)
#     return wynik
# print(wielokrotnosci(4))

#zadanie 8



#zadanie 9

# wielkosc = 25
# lista = np.arange(1,wielkosc+1,1)
# lista[1] = 1
# for i in range(2,wielkosc,1):
#     lista[i]=lista[i-1]+lista[i-2]
# macierzFib = lista.reshape([5,5])
# print(macierzFib)