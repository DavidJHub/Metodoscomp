#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;
double init(double x,double t);

int main () {
    int n=200;
    double xinicio=0;
    double xfin=1.0;
    double v=300.0;
    double dx=0.005;
    double dt=(dx/v)*0.5;
    double x[n];
    double t[n];


    for(int i = 0; i < n; i++)
    {
        x[i]=i*dx;
    }
    
    for(int i = 0; i < n; i++)
    {
        t[i]=i*dt;

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
    cout<<r;
    
    ofstream file2;
    file2.open ("Ufuturo.txt");
    for (int i=1; i<n-1;i++)
    {
        Afut[i] = Ainicial[i] + (r*r/2.0) * (Ainicial[i+1] - 2.0 * Ainicial[i] + Ainicial[i-1]);
    }
    
    for(int i =1; i<n-1;i++){
    file2 <<x[i]<< setw(20) << Afut[i] <<"\n";
    }
    
    double Aprt[n];
    double Apast[n];
    
    for (int i=1; i<n-1;i++)
    {
        Apast[i]=Ainicial[i];
        Aprt[i]= Afut[i];
        
    }
    
    double Afut0[n];
    double Afut1[n];
    double Afut2[n];
    double Afut3[n];
    
    
    /*Condicion inicial de extremos fijos*/
    
    ofstream file3;
    file3.open ("U.txt");
    for (int j=0;j<10000;j++){
        for (int i=1;i<n-1;i++){
            Afut[i] = (r*r)*(Aprt[i+1]+Aprt[i-1]-2*Aprt[i])-Apast[i]+2*Aprt[i];
        }
        
        
        if (j==10)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut0[k]= Afut[k];
            }
        }
        
        if (j==3000)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut1[k]= Afut[k];
            }
        }
        
        if (j==6000)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut2[k]= Afut[k];
            }
        }
        
        if (j==9000)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut3[k]= Afut[k];
            }
            for (int i=1;i<n-1;i++)
            {
                file3<<x[i]<< " " << Afut0[i]<< " "<< Afut1[i]<< " " << Afut2[i] << " " << Afut3[i]<<"\n";
            }
        }
      
        
        
        
        for (int l=1; l<n-1;l++)
        {
            Apast[l]=Aprt[l];
            Aprt[l]= Afut[l];

             
        }

     }
    
    /*Condicion inicial de un extremo libre*/
    
    for (int i=1; i<n-1;i++)
    {
        Afut[i] = Ainicial[i] + (r*r/2.0) * (Ainicial[i+1] - 2.0 * Ainicial[i] + Ainicial[i-1]);
        Afut[n-1] = Afut[n-2];
    }
    
    for(int i =1; i<n-1;i++){
    file2 <<x[i]<< setw(20) << Afut[i] <<"\n";
    }
    

    
    for (int i=1; i<n-1;i++)
    {
        Apast[i]=Ainicial[i];
        Aprt[i]= Afut[i];
        
    }
    
    
    
    ofstream file4;
    file4.open ("U2.txt");
    for (int j=0;j<10000;j++){
        for (int i=1;i<n-1;i++){
            Afut[i] = (r*r)*(Aprt[i+1]+Aprt[i-1]-2*Aprt[i])-Apast[i]+2*Aprt[i];
            Afut[n-1] = Afut[n-2];
        }
        
        
        if (j==10)
        {
            for (int k=1; k<n;k++)
            {
                Afut0[k]= Afut[k];
            }
        }
        
        if (j==3000)
        {
            for (int k=1; k<n;k++)
            {
                Afut1[k]= Afut[k];
            }
        }
        
        if (j==6000)
        {
            for (int k=1; k<n;k++)
            {
                Afut2[k]= Afut[k];
            }
        }
        
        if (j==9000)
        {
            for (int k=1; k<n;k++)
            {
                Afut3[k]= Afut[k];
            }
            for (int i=1;i<n;i++)
            {
                file4<<x[i]<< " " << Afut0[i]<< " "<< Afut1[i]<< " " << Afut2[i] << " " << Afut3[i]<<"\n";
            }
        }
      
        
        
        
        for (int l=1; l<n;l++)
        {
            Apast[l]=Aprt[l];
            Aprt[l]= Afut[l];

             
        }

     }
    
        /*Condicion inicial de un oscilador forzado
    
   
    for (int i=1; i<n-1;i++)
    {
        Ainicial[0]=cos(3.0∗v∗t[i]∗3.14)*0.1;
    }
    
    for (int i=1; i<n-1;i++)
    {
        Afut[i] = Ainicial[i] + (r*r/2.0) * (Ainicial[i+1] - 2.0 * Ainicial[i] + Ainicial[i-1]);
    }
    
    for (int i=1; i<n-1;i++)
    {
        Apast[i]=Ainicial[i];
        Aprt[i]= Afut[i];
        
    }
    
    ofstream file4;
    file4.open ("U3.txt");
    for (int j=0;j<10000;j++){
        for (int i=1;i<n-1;i++){
            Afut[i] = (r*r)*(Aprt[i+1]+Aprt[i-1]-2*Aprt[i])-Apast[i]+2*Aprt[i];
        }
        
        
        if (j==10)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut0[k]= Afut[k];
            }
        }
        
        if (j==3000)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut1[k]= Afut[k];
            }
        }
        
        if (j==6000)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut2[k]= Afut[k];
            }
        }
        
        if (j==9000)
        {
            for (int k=1; k<n-1;k++)
            {
                Afut3[k]= Afut[k];
            }
            for (int i=1;i<n-1;i++)
            {
                file3<<x[i]<< " " << Afut0[i]<< " "<< Afut1[i]<< " " << Afut2[i] << " " << Afut3[i]<<"\n";
            }
        }
      
        
        
        
        for (int l=1; l<n-1;l++)
        {
            Apast[l]=Aprt[l];
            Aprt[l]= Afut[l];

             
        }

     }*/
        
    
   return 0;
}

double init(double x,double t)
{
    double pendiente = 0.01/0.5;
    double A;
    if(x>0 && x<=0.5)
    {
        A=x*pendiente;
    }
    if(0.5<x && x<1)
    {
        A=0.02+x*(-pendiente);
    }
    return A;
}


