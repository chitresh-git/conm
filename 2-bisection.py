from sympy import *
import sympy
from decimal import* 
import matplotlib.pyplot as mp

getcontext().prec = 4

# def f(val):
#     return exp.subs(x,val)


n=input("enter the variable of your equation :")
x=Symbol(n)
# s=input()
exp=x*x-x-1



print(exp)


def f(c):
    return exp.subs(n,c)

print(f(2))
def bisection(a,b):
  global points
  points=[]
  e=0.000001
  if (f(a)*f(b) )>0:
    print("invalid interval ")
  else:
    i=1
    m=(a+b)/2
    while(abs(f(m))>e):
        if f(m)*f(a)>0:
            a=m
            
        else:
            b=m
        
        print(f"iteration={i}, a={a:6f} , b={b:6f} , m={m:6f} , f(m)={f(m)} ")
        m=(a+b)/2
        i+=1
        points.append(round(m,4))
    
    print(f"the roots is : {m}")
    print(points)


a,b=input("enter the value of a ,and b= ").split()
a=int(a)
b=int(b)
bisection(a,b)

plot(exp)  # use of sympy 

mp.plot(points,color="orange",marker='o',markersize=10)  # use of matplotlib
mp.show()
# mp.bar(x,points)
l=len(points)
y=[i*0 for i in range(l)]
mp.scatter(points,y)
mp.axhline(c="black",label="x-axis")
mp.show()

