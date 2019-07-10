#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;
double init(double x,double t);

int main () {
    int n=20000;
    double xinicio=0;
    double xfin=1.0;
    double v=300.0;
    double dx=(xfin-xinicio)/n;
    double dt=dx/v*3;
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
    
    ofstream myfileinit;
    myfileinit.open ("init.txt");
    double Ainicial[n];
    for (int i=1; i<n-1;i++)
    {
        Ainicial[i]=init(x[i],t[i]);
        myfileinit <<x[i]<< setw(20) << Ainicial[i] <<"\n";
    }
    
    Ainicial[0]=0;
    Ainicial[n-1]=0;
    double Afut[n];
    Afut[0]=0;
    Afut[n-1]=0;
    double r=v*(dt/dx);
    
    ofstream file2;
    file2.open ("Ufuturo.txt");
    for (int i=1; i<n-1;i++)
    {
        Afut[i] = Ainicial[i]+(r*r/2.0)*(Ainicial[i+1]-2.0*Ainicial[i]+Ainicial[i-1]);
        file2 <<x[i]<< setw(20) << Afut[i] <<"\n";
    }
    
    double Apast[n];
    
    for (int i=1; i<n-1;i++)
    {
        Apast[i]=Ainicial[i];
    }
    double Aprt[n];
    for (int i=1; i<n-1;i++)
    {
        Aprt[i]= Afut[i];
    }
    
    for (int i=0;i<n;i++){
        for (int j=1;j<n-1;j++){
            
            Afut[i]=(2.0*(1.0-r*r))*Aprt[i]-Apast[i]+(r*r)*(Aprt[i+1]+Aprt[i-1]);
        }
    }
   return 0;
}

double init(double x,double t)
{
    double A=0.01;
    if(x>0 && x<0.5)
    {
        A=x*0.0198994;
    }
    if(0.5<x && x<1)
    {
        A=0.02+x*(-0.0198994);
    }
    return A;
}


