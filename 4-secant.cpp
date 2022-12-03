#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

// program to find roots of equation using secant method 
// by - chitresh mourya 

float f(float x)
{
    return x * x * x - 5 * x + 1;
}

int main()
{
    float x0, x1,f0,f1, e = 0.0000001, Xi;
    int i = 0;
    
    cout<<"please enter two approximation points : "<<endl;
    cout << "enter the value of a : " << endl;
    cin >> x0;
    cout << "enter the value of b:" << endl;
    cin >> x1;

    
    if (0)
    {
        cout << "invalid interal , enter different vlaues (a=0,b=1) " << endl;
    }
    else
    {

        i = 1;
     

        while (fabs(f(x1)) > e)
        {

            f1 = f(x1);
            f0 = f(x0);

            Xi = (f1 * (x1 - x0)) / (f1 - f0);
            Xi = x1 - Xi;

            x0 = x1;
            x1 = Xi;

            i++;
            cout << "k";
            printf(" iteration=%d  X%d =%f \n", i, i, Xi);
        }

        cout << "the root is = " << Xi << endl;
    }
}