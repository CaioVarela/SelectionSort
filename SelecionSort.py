from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import timeit

tamanho = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]

def gerarLista(tam):
    lista = []
    while len(lista) < tam:
        x = randint(1,1*tam)
        if x not in lista: lista.append(x)
    return lista

def selection_sort(lista):
  n= len(lista)
  for j in range(n-1):
    min_index = j
    for i in range(j,n):
      if lista[i] < lista[min_index]:
        min_index = i
    if lista[j] > lista[min_index]:
      aux = lista[j]
      lista[j] = lista[min_index]
      lista[min_index] = aux
      
mpl.use('Agg')
def gerarGrafico(x,y,z):    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Caso")
    ax.plot(x,z, label = "Pior Caso")    
    plt.xlabel('TAMANHO DA LISTA')
    plt.ylabel('TEMPO DE ORDENAMENTO')      
    fig.savefig('graph.png')

Melhor_Caso = []
Pior_Caso = []

for i in tamanho:
  normal = gerarLista(i)
  melhor = sorted(normal)
  pior = sorted(normal, reverse=True)
  Melhor_Caso.append(timeit.timeit("selection_sort({})".format(melhor),setup="from __main__ import selection_sort",number=1))
  Pior_Caso.append(timeit.timeit("selection_sort({})".format(pior),setup="from __main__ import selection_sort",number=1))

gerarGrafico(tamanho,Melhor_Caso,Pior_Caso)