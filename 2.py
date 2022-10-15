N = int(input("Введите количество элементов массива 1: "))
D = [0]*N
from random import randint
for i in range(N): 
  D[i] = randint(1, 10)
print(D) 
B = int(input("Введите количество элементов массива 2: "))
M = [0]*B
from random import randint
for i in range(B):
    M[i] = randint(1, 10)
print(M)
L = []
for i in M:
     if i in D and i not in L:
            L.append(i)
print(L)   

          