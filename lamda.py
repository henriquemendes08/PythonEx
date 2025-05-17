from functools import reduce
fatorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1 ))
print(fatorial)

print(fatorial(5))  