import sys
x = []
sizes = [sys.getsizeof(x)]

for i in range(0, 100):
    x.append(1)
    sizes.append(sys.getsizeof(x))

print(sizes)
