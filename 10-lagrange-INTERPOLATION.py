def lagrange():

       n=int(input("enter the number of elements in table- "))
       x=[]
       f=[]
       print(f"please enter {n} data entries : ")
       
       for i in range(n):
          xi=float(input(f"enter x{i+1} = "))
          fi=float(input("enter f(x) ="))
          x.append(xi)
          f.append(fi)
       print("\n\nthe entered table is : ")
       for e in zip(x,f):
         print(e)

       term=float(input("\n\nenter at which point , you want to find the value of funciton : "))
       sum=0
       for i in range(n):
            prodf=1
            for j in range(n):
                if j!=i:
                    temp=(term-x[j])/(x[i]-x[j])
                    prodf=prodf*temp
            
            sum=sum+(f[i]*prodf)
        

       print(f"\n\nthe value of funciton at x={term} is  : {sum}")


lagrange()