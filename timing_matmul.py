from scipy import matmul, rand
from time import perf_counter

N = 3

A = rand(N,N)
B = rand(N,N)

t1 = perf_counter()
C = A@B        #Python 3.5 o mas define el operador `@` como multiplicacion de matrices. 
			   # Si no le funciona, usar la funcion `matmul`
			   #
			   # Se recomienda no usar la clase 'matrix'.
			   #
#C = matmul(A,B)
t2 = perf_counter()

dt = t2 - t1

print(f"Tiempo transcurrido = {dt} s")



