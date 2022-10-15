N = int(input("Введите количество элементов массива: "))
D = [0]*N
from random import randint
for i in range(N): 
  D[i]  = randint(-100, 100)
print(D) 
a = D[0]
for i in range(1, N):
   if D[i]>a:
    a = D[i]
    n = i
for i in range(N):
    if i>n:
     D[i]=0
print(D)