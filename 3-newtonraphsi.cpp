#include<iostream>
using namespace std;
#include<math.h>

// program to find roots of equation using newton-raphsi  method 
// by - chitresh mourya 

double f(double x){
    return x*x*x-3*x-5;
}

double df(double x){
    return 3*x*x-3;
}

int main(){
    double a , x0 , x1,e=0.000001;
    int i;

    cout<<"enter any assumed root : "<<endl;
    cin>>a;

    x0=a;

     

    i=1;
    double temp;
    while(fabs(f(x0))>e){
      temp= f(x0)/df(x0);
      x1=x0- temp;

      x0=x1;
      cout<<i;
      cout<<"__this is value of x"<<i-1<<" = "<<x0<<endl;
      i++;
    }

    cout<<"the root is : "<<x0;

return 0;

}