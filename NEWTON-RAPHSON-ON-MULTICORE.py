from math import fabs
from sympy import *
import multiprocessing as mp
import time



x=Symbol('x')
eq=x**2+2*x-2
dq=diff(eq,x)



rs=Poly(eq,x).nroots()
print("the roots of equation = ", rs)


def newton():
    i=0
    print(f"the equation is : {eq}")
    # x0=int(input("enter any approximation point : "))
    x0=10

    e=0.00000000000001

    while fabs(eq.subs(x,x0))>e:
        i=1+i
        temp= eq.subs(x,x0)/dq.subs(x,x0)
        temp=float(temp)

        x1=x0-temp

        x0=x1

        print(f"the value of x{i} is = {x0:4f}")
    
    print(f"the root is : {x0:4f}")

    plot(eq)







if __name__=='__main__':
    print("Number of logical CPU's available in this pc :", mp.cpu_count())
    pool=mp.Pool(mp.cpu_count())
    pool.apply_async(newton())
   
    ts=time.time()
    pool.close()
    pool.join()
    
    print("Time taken to compute this code is : ", time.time() - ts)

