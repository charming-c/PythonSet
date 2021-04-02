x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))
a, b = zip(*zip(x, y))
print(a)
print(b)
