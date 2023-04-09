import random
import math

sz = 8

a = [[0 for j in range(sz)] for i in range(sz)]
for i in range(sz):
    a[i][0] = random.getrandbits(1)
    print(a[i][0], end='')
print()

#ans = input()

#cамодвойственность
selfdual = True
for i in range(0, sz):
        if a[i] == a[sz - i - 1]:
            selfdual = False


#линейность
for j in range(1, sz):
    for i in range(j, sz):
        a[i][j] = a[i][j - 1] ^ a[i - 1][j - 1]
linear = True
for i in range(0, sz):
    if a[i][i]:
        j = i
        check = True
        while j != 1 and j != 0:
            if j % 2 == 1:
                check = False
            j /= 2
        if not check:
            linear = False

#монотонность
n = int(math.log2(len(a)))
monot = True
for i in range(1 << n):
    temp = i
    for j in range(n):
        if temp % 2 == 0:
            index = i + (1 << j)
            if a[i] > a[index]:
                monot = False
        temp //= 2

#F0 F1
F0 = True
if a[0] == 1:
    F0 = False

F1 = True
if a[sz - 1] == 0:
    F1 = False

if F1:
    print("Сохраняющая единицу")

if F0:
    print("Сохраняющая ноль")

if monot:
    print("Монотонная")

if linear:
    print("Линейная")

if selfdual:
    print("Самодвойственная")



