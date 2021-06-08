dt = {x: x ** 2 for x in range(1, 10)}
print(dt)

dt = {x: x ** 2 for x in range(1, 10)}
print(dt)

dt = {x: y for x in range(1, 10) for y in range(3, 7)}
print(dt)

dt = {x: x * 100 + y for x in range(1, 10) for y in range(3, 7)}
print(dt)

dt = {x * 10 + y: y * 100 for x in range(1, 10) for y in range(3, 7)}
print(dt)