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
L = []
if N==B:
  for i in M:
     if i in D:
            L.aapend(i)
            print(L)
else:
    print("GG")  
    #не получилось придумать,что делать,если размерность массивов отличается          