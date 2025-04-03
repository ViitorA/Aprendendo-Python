# Em Python você pode mudar o tipo da variável
x = y = z = 5 # Atribuir o mesmo valor a n variáveis
x = "Victor" # 'Victor' = "Victor"

print(x)

# ==========| CASTING |==========
# x = '3', y = 3, z = 3.0
x, y, z = str(3), int(3), float(3)
print(type(x),type(y),type(z))
x = int("3") # x = 3
print(type(x))

# ==========| NOME DE VARIÁVEL |==========
minhaVariavel = 3  # Camel Case
MinhaVariavel = 3  # Pascal Case
minha_variavel = 3 # Snake Case

# ==========| UNPACKING |==========
frutas = ["maçã", "banana", "morango"]
# x = maçã, y = banana, z = morango
x, y, z = frutas

print(x, y, z)

# ==========| Variável Global |==========
# Qualquer variável declarada fora de uma função é global. Caso queira criar uma variável global dentro de uma função, use a palavra-chave 'global'
# Você pode usar a palavra-chave global também para alterar o valor de uma variável global dentro de uma função.

def minhaFuncao():
    global delta
    delta = -4

    global x 
    x = "Função"

minhaFuncao()
print("O delta é", delta)
print(x)

# ==========| DATA TYPES |==========
# str
x = "Hello World" # Ou, se você quiser especificar: x = str("Hello World")
# int
x = 20
# float
x = 2.0
# complex
x = 1j # ou x = complex(1j)
# list
x = ["Maçã", "Banana"]
# tuple
x = ("Maçã", "Banana")
# range
x = range(6)
# dict
x = {"Nome": "Victor", "idade":20}
# set
x = {"Maçã", "Banana"}
# frozenset
x = frozenset({"Maçã","Banana"})
# bool
x = True
# bytes
x = b"Hello"
# bytearray
x = bytearray(5)
# memoryview
x = memoryview(bytes(5))
# NoneType
x = None

# ==========| RANDOM |==========
import random
print(random.randrange(1,10))
