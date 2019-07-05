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
    myfile.open ("EULER.txt");
    
    cout << setw(4) << "X"
         << setw(4) << "Y";
     
    for(int i=1;i<n;i++)
    {
        float p=funcion(x[i-1],y[i-1]);
        x[i]=x[i-1]+h;
       
        cout << x[i] << endl;
        y[i]=y[i-1]+h*(p);
        cout << y[i] << endl;
        myfile <<x[i]<< setw(4) << y[i] <<"\n";
        
    }
    
    

   return 0;
}

float funcion(float x,float y)
{
    return -y;
}



