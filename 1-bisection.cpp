#include<iostream>
#include<stdio.h>
using namespace std;
#include<math.h>

// program to find roots of equation using bisection method 
// by - chitresh mourya 

float f(float x){
    // return (x*x-x-1);
    return (x*x-x-1);
}

int main(){
    float a,b,m,e=0.000001;
    int i=0;
    cout<<"enter value of a and b respectively :"<<endl;
    cout<<"enter the value of a ="<<endl;
    cin>>a;
    cout<<"enter the value of b ="<<endl;
    cin>>b;

    if ((f(a)*f(b)) >0){
        cout<<" invalid interval , enter agian"<<endl;

    }
    else{
        m=(a+b)/2;
        i=1;

        while(fabs(f(m))>e){
            cout<<"iteration="<<i<<" ; a="<<a<<" ; b="<<b<<" ; f(m)="<<f(m)<<endl;
            if(f(a)*f(m)>0){
                a=m;
            }
            else{
                b=m;
            }
            m=(a+b)/2;
            i++;
        }
        printf(" root is = %f",m);
    }
return 0;

}