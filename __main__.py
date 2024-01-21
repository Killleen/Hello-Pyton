#Задача 4
print(int(-5.7))
print(int(-5.7))
print(int(float(3 ** 39)))

#Задача 5
print('Hi,', input('Введите имя: '))

#Задача 6
print((int(input('Введите X: ')) * 60
       + int(input('Введите Y: '))) * 2)

#Задача 7
print((not False or True) and False)
#Задача 8
dr = int(input('Введите год рождения: '))
if (dr < 1900 or dr > 3000):
    print("Год не входит в выборку")
else:
    print('С днём рождения!' if dr % 4 == 0 and dr % 100 != 0 or dr % 400 == 0 else 'Год обычный')
#Задача 9
i = 0;
while (i < 20):
    i += 2
    print(i)
#Задача 10
a = int(input())
sum = a
while (a != 0):
    a = int(input())
    sum += a
else:
    print(sum)

#Задача 11
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

#Задача 12
for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=" ")

#Задача 13
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

#Задача 14
n = int(input('Введите размер матрицы: '))
matrix = [[0] * n for _ in range(n)]
num = 1
left, right, top, bottom = 0, n - 1, 0, n - 1

while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for row in matrix:
    for num in row:
        print(num, end='\t')
    print()

#Задача 15
import time
from tkinter import messagebox

if __name__ == '__main__':
    while (True):
        time.sleep(10)
        messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')
