#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

double funcion1(float x,float t,float v);
double funcion2(float x,float t,float v);


int main () {
    int n=1000;
    double tinicio=0;
    double tfin=364;
    double h=(tfin-tinicio)/n;
    double x[n];
    double y[n];
    double z[n];
    
    double t[n];
    double v[n];

    //Se toman las condiciones 
    x[0]=0.168267;
    y[0]=0.970040;
    z[0]=-0.000035;
    t[0]=tinicio;
    v[0]=0;
    
    
    ofstream myfile;
    myfile.open ("Orbita.txt");

    for(int i=1;i<n;i++)
    {
        double k1_1 = funcion1(x[i-1],t[i-1],v[i-1]);
        double k1_2 = funcion2(x[i-1],t[i-1],v[i-1]);
            
        double t1 = t[i-1]+(h/2);
        double x1 = x[i-1]+(h/2)*k1_1;
        double v1 = v[i-1]+(h/2)*k1_2;
        
        double k2_1 = funcion1(x1,t1,v1);
        double k2_2 = funcion2(x1,t1,v1);
        
        double t2 = t[i-1]+(h/2);
        double x2 = x[i-1]+(h/2) * k2_1;
        double v2 = v[i-1]+(h/2) * k2_2;
            
            
        double k3_1 = funcion1(x2, t2, v2);
        double k3_2 = funcion2(x2, t2, v2);
        
        double t3 = t[i-1]+h;
        double x3 = x[i-1]+h*k3_1;
        double v3 = v[i-1]+h*k3_2;
        
        
        double k4_1 = funcion1(x3,t3,v3);
        double k4_2 = funcion2(x3,t3,v3);
        
        double k1prom = (1.0/6.0)*(k1_1 + 2.0*k2_1 + 2.0*k3_1 + k4_1);
        double k2prom = (1.0/6.0)*(k1_2 + 2.0*k2_2 + 2.0*k3_2 + k4_2);
         
        
        t[i]=t[i-1]+h;
        x[i]=x[i-1]+h*k1prom;
        v[i]=v[i-1]+h*k2prom;

        cout << t[i] << endl;
        cout << x[i] << endl;
        cout << v[i] << endl;
        

        
/*
        cout << k1_1 << endl;
        cout << k1_2 << endl;
        cout << k2_1 << endl;
        cout << k2_2 << endl;
        cout << k3_1 << endl;
        cout << k3_2 << endl;
        cout << k4_1 << endl;
        cout << k4_2 << endl;
*/

        


        myfile <<t[i]<< setw(20) << x[i] <<setw(20) << v[i]<<"\n";


    }
    
    
    

   return 0;
}


double funcion1x(float x,float y,float z, float t, float vx)
{
    return vx;
}


double funcion2(float x,float y,float z,float t, float vx)
{
    double g=300;
    double m=2;
    return -(g*m)/(x*x+y*y+z*z);
}
