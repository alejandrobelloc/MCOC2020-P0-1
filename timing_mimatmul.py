from scipy import rand
from mimatmul import mimatmul
from time import perf_counter

N = 3

A = rand(N,N)
B = rand(N,N)

t1 = perf_counter()
C = mimatmul(A,B)
t2 = perf_counter()

dt = t2 - t1

print(f"Tiempo transcurrido = {dt} s")



