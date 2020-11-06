
v = int(input("Скорость Васи: "))
t = int(input("Время в пути: "))

if v > 0:
    s = (v * t) % 100
else:
    s = 0 - (-v * t) % 100
print(s)