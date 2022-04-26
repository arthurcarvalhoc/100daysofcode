## Lambda

x = lambda a : a + 10
print(x(5))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


## Arrays

cars = ["Ford", "Volvo", "BMW"]

x = len(cars)
print(x)

for x in cars:
  print(x)

cars.append("Honda")
cars.pop(1)

cars.remove("Volvo")