print('hello world')

x = 2022
y = "Arthur Carvalho"
print(type(x))
print(type(y))

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = "Arthur Carvalho"
print(x , y)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = 4
y = 5
# conferindo os valores das variáveis
print(x, y)

# instanciando a variável auxiliar
temp = x
x = y
y = temp
# conferindo a troca
print(x, y)

# instanciando a variável auxiliar

x = x + y
y = x - y
x = x - y
# conferindo a troca
print(x, y)


# Utilizando operado XOR Bitwise
# Ou operação binária
x = x ^ y
y = x ^ y
x = x ^ y

# conferindo a troca
print(x, y)