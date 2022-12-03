from sympy import *
# 27.10.22
# program to solve the equation using the gauss siedal method

def siedal_static():
      var="x,y,z"
      x,y,z=symbols(var)

      e1=Eq((27*x+6*y-z),85)
      print(e1)
      v=6*x+15*y-z
      e2=Eq((v),72)
      e3=Eq((x+y+54*z),110)

      result=solve((e1,e2,e3),(x,y,z))
      print(float(result.get(x)))


      xn=solve(e1,x)  # this will return the x seperated equation which is stored inside the list 
      xe=xn[0] # extracting the x oriented equation from the list 
      yn=solve(e2,y)   
      ye=yn[0] 
      zn=solve(e3,z)  
      ze=zn[0] 

      x0,y0,z0=0,0,0

 
      x_next=1
      count=0

      
 
      while x0!=x_next:
       print("\n\niteration=",count)

       x_next=round(float(xe.subs([(z,z0),(y,y0)])),4)
       print("x=",x_next)
       
       y_next=round(float(ye.subs([(z,z0),(x,x0)])),4)
       print("y=",y_next)

       z_next=round(float(ze.subs([(y,y0),(x,x0)])),4)
       print("z=",z_next)

  
       x0=x_next
       y0=y_next
       z0=z_next

       x_next=round(float(xe.subs([(z,z0),(y,y0)])),4)
       count+=1


siedal_static()


