#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

float funcion(float x,float y);

int main () {
    int n=100;
    float inicio=0;
    float fin=2;
    float h=(fin-inicio)/n;
    float y[n];
    float x[n];
    for ( int i=1;i<n; i++){
        y[i]=0;
    }
    for  ( int i=1;i<n; i++){
        x[i]=0;
    }
    x[0]=inicio;
    y[0]=1;
    
    
    ofstream myfile;
    myfile.open ("RK.txt");
    
    cout << setw(4) << "X"
         << setw(4) << "Y";
    for(int i=1;i<n;i++)
    {
        float k1 = h*funcion(x[i-1],y[i-1]);
        float k2 = h*funcion(x[i-1]+0.5*h,y[i-1]+0.5*k1);
        float k3 = h*funcion(x[i-1]+0.5*h,y[i-1]+0.5*k2);
        float k4 = h*funcion(x[i-1]+h,y[i-1]+k3);
            
        float kprom = (1.0/6.0)*(k1+2.0*k2+2.0*k3+k4);
        x[i]=x[i-1]+h;
        y[i]=y[i-1]+kprom;
        cout << x[i]<< endl;
        cout << y[i] << endl;
        myfile <<x[i]<< setw(4) << y[i] <<"\n";


    }
    
    

   return 0;
}

float funcion(float x,float y)
{
    return -y;
}



