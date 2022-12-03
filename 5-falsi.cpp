#include <iostream>
#include <stdio.h>
using namespace std;
#include <math.h>

// program to find roots of equation using regular falsi method 
// by - chitresh mourya 

double f(double x)
{
    // return (x*x-x-1);
    return x*x-x-1;
}

int main()
{
    float a, b, m, e = 0.0001;
    int i = 0;
    cout << "enter value of a and b respectively :" << endl;
     cout<<"enter the value of a ="<<endl;
    cin>>a;
    cout<<"enter the value of b ="<<endl;
    cin>>b;

    printf("f(a)=%f",f(a));
    printf("f(b)=%f",f(b));

    if (f(a) * f(b) > 0)
    {
        cout << "invalid interval " << endl;
    }

    else
    { 
        float n1,n2,d1,d2;

      

         m=(a*f(b)- b*f(a)) / (f(b)-f(a));    //// the bracketing of this expression is most important 


        i = 1;
       

        while (fabs(f(m)) > e)
        {   
            
            printf("iteration =%d , a=%f , b=%f  , f(m)=%f", i, a, b, f(m));
            printf("\n\n");

            if (f(a) * f(m) > 0)
            {
                a = m;
            }
            else
            {
                b = m;
            }

        m=( a*f(b)- b*f(a) ) / ( f(b) - f(a) ) ;  // the bracketing of this expression is most important 
        i++;

        }

        printf(" the root is = %f", m);
    }
    return 0;
}
