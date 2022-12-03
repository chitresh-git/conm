from math import fabs
from sympy import *
import matplotlib.pyplot as ml
import multiprocessing as mp

import time

x, y = symbols('x,y')
def case1():
     #case1: - 
     eq1=Eq((2.5000*x+5.2000*y),6.200)
     eq2=Eq((1.251*x+2.605*y),3.152)
     time.sleep(2)

     print("\n\n",eq1)
     print(eq2)

     case1=solve((eq1, eq2), (x, y))
     print("\nanswer of case 1 : ",case1)


     #case2: -
def case2(): 
      eq21=Eq((2.5000*x+5.2000*y),6.200)
      eq22=Eq((1.251*x+2.606*y),3.152)

      print("\n\n",eq21)
      print(eq22)

      case2=solve((eq21, eq22), (x, y))
      print("\nanswer of case 2 : ",case2)

def case3(): 
      eq31=Eq((0.00002*x+2.0000*y),2.0000)
      eq32=Eq((1*x+2*y),4)

      print("\n\n",eq31)
      print(eq32)

      case3=solve((eq31, eq32), (x, y))
      print("\nanswer of case 3 : ",case3)
def case4(): 
      
      eq41=Eq((1*x+2.0000*y),2.0000)
      eq42=Eq((0.00002*x+2*y),4)

      print("\n\n",eq41)
      print(eq42)

      case4=solve((eq41, eq42), (x, y))
      print("\nanswer of case 4 : ",case4)

# sysEq()

if __name__=='__main__':
    print("Number of logical CPU's available in this pc :", mp.cpu_count())
    pool=mp.Pool(mp.cpu_count()) 
    pool.apply_async(case1(),case2(),case3(),case4())
    ts=time.time()
    pool.close()
    pool.join()
    
    print("Time taken to compute this code is : ", time.time() - ts)

