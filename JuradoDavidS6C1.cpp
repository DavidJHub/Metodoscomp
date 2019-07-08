#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;
double init(double x,double t);

int main () {
    int n=100;
    double xinicio=0;
    double xfin=2.0;
    double v=1.0;
    double dx=(xfin-xinicio)/n;
    double dt=dx/v*0.25;
    double x[n];
    double t[n];

    
    

    for(int i = 0; i < n; i++)
    {
        x[i]=i*dx;
    }
    
    for(int i = 0; i < n; i++)
    {
        t[i]=i*dt;
        cout << t[i] << endl;
    }
    
    double A[n];
    for (int i=1; i<n-1;i++)
    {
        A[i+1]=v*dt/dx*(init(x[i],t[i])-init(x[i-1],t[i]))+init(x[i],t[i])
    }
    
    
    /**
    ofstream myfile;
    myfile.open ("Resorte.txt");

    for(int i=1;i<n;i++)
    {
        
        


        myfile <<t[i]<< setw(20) << x[i] <<setw(20) << v[i]<<"\n";


    }
    
    **/
    

   return 0;
}

double init(double x,double t)
{
    double A=1.0;
    if(0.75<x<1.25)
    {
        A=2.0;
    }
}


