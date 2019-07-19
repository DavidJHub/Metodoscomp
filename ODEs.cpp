#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

double funcion1x(double t, double x, double vx);
double funcion1y(double t, double y, double vy);
double funcion2x(double t, double x, double y,double vx, double vy);
double funcion2y(double t, double x, double y,double vx, double vy);


int main () {
    int n=50000;
    double tinicio=0;
    double tfin=1;
    double dt=(tfin-tinicio)/n;



    
    double t[n];
    
    
    double x_1[n];
    double x_2[n];
    double y_1[n];
    double y_2[n];
    
    double r[n];
    
    
    //Se toman las condiciones 
    x_1[0]= 0.1163;
    y_1[0]= 0.9772;
    r[0]= sqrt(x_1[0]*x_1[0]+y_1[0]*y_1[0]);
    
    
    x_2[0]=-6.35;
    y_2[0]=0.606;
    

    
    t[0]=tinicio;
    
    
    
    ofstream euler;
    euler.open ("OrbitaEuler.txt");
    
    
    
    //###########################################euler#############################################################################
    for (int i=1;i<n;i++){
        

        double x_prima_1 = funcion1x(t[i-1],x_1[i-1],x_2[i-1]);
        double y_prima_1 = funcion1y(t[i-1],y_1[i-1],y_2[i-1]);
            
            
        t[i] = t[i-1] + dt;
        x_1[i] = x_1[i-1] + dt*x_prima_1;
        y_1[i] = y_1[i-1] + dt*y_prima_1;
        
        

            
            
        double x_prima_2 = funcion2x(t[i-1],x_1[i-1],y_1[i-1],x_2[i-1],y_2[i-1]);
        double y_prima_2 = funcion2y(t[i-1],x_1[i-1],y_1[i-1],x_2[i-1],y_2[i-1]);
            
 
        x_2[i] = x_2[i-1] + dt*x_prima_2;  
        y_2[i] = y_2[i-1] + dt*y_prima_2;

        
        r[i]=sqrt(x_1[i]*x_1[i]+y_1[i]*y_1[i]);
        euler <<t[i]<< " " << x_1[i] << " " << y_1[i] << " " << x_2[i]<< " " << y_2[i] << " " << r[i] <<"\n";
    }
    
    
    //leap frog
    
    
        //Se toman las condiciones 
    t[0]=tinicio;
    t[1]=tinicio + h
    
    x_1[0]= 0.1163;
    y_1[0]= 0.9772;

    r[0]= sqrt(x_1[0]*x_1[0]+y_1[0]*y_1[0]);
    
    
    
    x_2[0]=-6.35;
    y_2[0]=0.606;
    
    x_1[1]= x_1[0]+h*funcion1x(t[0], x_1[0], x_2[0])
    y_1[1]= y_1[0]+h*funcion1y(t[0], x_1[0], x_2[0])
    
    x_2[1]= x_2[0]+h*funcion2x(t[0],x_1[0],y_1[0],x_2[0],y_2[0])
    y_2[1]= y_2[0]+h*funcion2y(t[0],x_1[0],y_1[0],x_2[0],y_2[0])


    
    
    for (int i=1;i<n;i++){
        

        double x_prima_1 = funcion1x(t[i-1],x_1[i-1],x_2[i-1]);
        double y_prima_1 = funcion1y(t[i-1],y_1[i-1],y_2[i-1]);
            
            
        t[i+1] = t[i-1] + dt;
        x_1[i] = x_1[i-1] + dt*x_prima_1;
        y_1[i] = y_1[i-1] + dt*y_prima_1;
        
        

            
            
        double x_prima_2 = funcion2x(t[i-1],x_1[i-1],y_1[i-1],x_2[i-1],y_2[i-1]);
        double y_prima_2 = funcion2y(t[i-1],x_1[i-1],y_1[i-1],x_2[i-1],y_2[i-1]);
            
 
        x_2[i] = x_2[i-1] + dt*x_prima_2;  
        y_2[i] = y_2[i-1] + dt*y_prima_2;

        
        r[i]=sqrt(x_1[i]*x_1[i]+y_1[i]*y_1[i]);
        euler <<t[i]<< " " << x_1[i] << " " << y_1[i] << " " << x_2[i]<< " " << y_2[i] << " " << r[i] <<"\n";
    }
    
        
    
        
      /*  
        
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
        */

        
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

        


        

    

   return 0;
}


double funcion1x(double t, double x, double vx)
{
    return vx;
}

double funcion1y(double t, double y, double vy)
{
    return vy;
}

double funcion2x(double t, double x, double y,double vx, double vy)
{
    double g=39.478;
    double m=1;
    return -(g*m)*x/pow(sqrt((x*x+y*y)),3);
}
double funcion2y(double t, double x, double y,double vx, double vy)
{
    double g=39.478;
    double m=1;
    return -(g*m)*y/pow(sqrt((x*x+y*y)),3);
}