# 4
print(int(-5.7))
print(int(-5.7))
print(int(float(3 ** 39)))

# 5
print('Hi,', input('Введите имя: '))

# 6
print((int(input('Введите X: ')) * 60
       + int(input('Введите Y: '))) * 2)

# 7
print((not False or True) and False)
# 8
dr = int(input('Введите год рождения: '))
if (dr < 1900 or dr > 3000):
    print("Год не входит в выборку")
else:
    print('С днём рождения!' if dr % 4 == 0 and dr % 100 != 0 or dr % 400 == 0 else 'Год обычный')
# 9
i = 0;
while (i < 20):
    i += 2
    print(i)
# 10
a = int(input())
sum = a
while (a != 0):
    a = int(input())
    sum += a
else:
    print(sum)

# 11
x = int(input())
y = int(input())
if x > y:
    max = x
else:
    max = y
kus = max
while (True):
    if ((kus % x == 0) and (kus % y == 0)):
        break
    kus += max

if (kus % 2 == 0):
    print(kus)
else:
    print(kus * 2)

# 2ое решение
import math

x = int(input())
y = int(input())
kus = math.lcm(x, y)
if (kus % 2 == 0):
    print(kus)
else:
    print(kus * 2)

# 12
for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=" ")

# 13
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
print(end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()

# 14
n = int(input("N: "))
a = [[0 for j in range(n)] for i in range(n)]
x, y = 0
dx, dy = 0, 1
a[0][0] = 1
count = 2
while count <= n * n:
    if (x + dx >= 0 and x + dx <= n - 1 and y + dy <= n - 1 and y + dy >= 0 and a[x + dx][y + dy] == 0):
        a[x + dx][y + dy] = count
        count += 1
        x += dx
        y += dy
    elif (dy == 1):
        dx = 1
        dy = 0
    elif (dx == 1):
        dx = 0
        dy = -1
    elif (dy == -1):
        dx = -1;
        dy = 0;
    elif (dx == -1):
        dx = 0
        dy = 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end='\t')
    print()

# 15
import time
from tkinter import messagebox

if __name__ == '__main__':
    while (True):
        time.sleep(10)
        messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')