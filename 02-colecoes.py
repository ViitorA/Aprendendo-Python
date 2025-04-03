# O Python possui 4 data types para guardar coleções de dados: Listas, Tuples, Set e Dictionary 
# Listas: Ordenado, Mutável e valores duplicados permitidos;
# Tuples: Ordenado, Imutável e valores duplicados permitidos;
# Sets: Não ordenado, Imutável* e não indexado, logo valores duplicados não são permitidos;
# Dictionary: Ordenado**, Mutável e valores duplicados não são permitidos.
#
# *Itens de sets são imutáveis, mas você pode adicionar e remover itens;
# **A partir do Python 3.7, dicionários são ordenados, mas do Python 3.6 para trás não são.

# ==========| LISTAS |==========
# Em lista, os itens são ordenados, mutáveis e é permitidos valores duplicados.
# São ordenados pois tem uma ordem definida que não se altera. Se você adiciona novos itens, eles vão para o final da lista.
# São mutáveis pois nós podemos mudar, adicionar e remover itens em uma lista depois que já fora criada.
# Começa com index 0, 1, 2...
essaLista = ["Maçã", 25, True] # Ou podemos usar também: essaLista = list(("Maçã", 25, True))
print(essaLista)

# P/a determinar o tamanho de uma lista podemos usar o len()
print(len(essaLista))
print(type(essaLista))
