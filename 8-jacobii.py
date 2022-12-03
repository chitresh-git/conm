from sympy import *
# 22.10.22
# program to solve the equation using the jacobi method

def jacobi_static():
      var="x,y,z,"
      x,y,z=symbols(var)

      e1=Eq((27*x+6*y-z),85)
      print(e1)

      e2=Eq((6*x+15*y-z),72)
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
       x0=x_next
       
       y_next=round(float(ye.subs([(z,z0),(x,x0)])),4)
       print("y=",y_next)
       y0=y_next

       z_next=round(float(ze.subs([(y,y0),(x,x0)])),4)
       print("z=",z_next)
       z0=z_next

  

       x_next=round(float(xe.subs([(z,z0),(y,y0)])),4)
       count+=1


#jacobi_static()


def jacobi_user():
          n=int(input("enter the number of coefficients in your equation :"))
          var=""
          for i in range(n):
            var+="x"+str(i)+","
          print(var)

      #     symbols=x


          n_eq=int(input("enter the number of equations : "))

          print(f"now enter the values for system of {n_eq} equations in the 2-d array :")
          
          lists=var.split(",")
          outer=[]
          for i in range(n_eq):
            inner=[]

            
            for j in range(n+1):
                  e=int(input("insert for:"))
                  inner.append(e)
            
            outer.append(inner)

          

          print(outer)
          from numpy import array
          ar=array(outer)
          print(ar)
          print(ar[1][0])


      #     sub_eq=
      #     for i in range(n)





# jacobi_user()
          
