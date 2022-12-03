def forward():

       n=int(input("enter the number of elements in table- "))
       x=[]
       f=[]
       print(f"please enter {n} data entries : ")
       
       for i in range(n):
        
          fi=float(input(f"enter f(x{i+1}) ="))
       
          f.append(fi)
       print("\n\nthe entered table is : ")
       for e in f:
            print(e)

        
       matrix=[]
   
       for j in range(n):
          temp=[]
          for i in range(1,n-j):
             if j==0:
                res=f[i]-f[i-1]
                temp.append(res)
                
                
             else:
               
                res=matrix[j-1][i]-matrix[j-1][i-1]
                temp.append(res)
           
          matrix.append(temp)
       
          
       print("\nso the diffrence table is :")
       for i in range(len(matrix)-1):
           print(f"\n {i+1} forward differece :-")
           print(matrix[i])
        
       

forward()