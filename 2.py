N = int(input("Введите количество элементов массива 1: "))
D = [0]*N
from random import randint
for i in range(N): 
  D[i] = randint(1, 2)
print(D) 
B = int(input("Введите количество элементов массива 2: "))
M = [0]*B
from random import randint
for i in range(B):
    M[i] = randint(1, 2)
print(M)
if N==B:
    a = 0
    for i in range(B):
        if D[i]==M[i]:
            a = D[i]
            print(a)
else:
    print("GG")            