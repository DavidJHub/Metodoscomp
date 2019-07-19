#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

double funcion1x(double t, double x, double vx);
double funcion1y(double t, double y, double vy);
double funcion2x(double t, double x, double y,double vx, double vy);
double funcion2y(double t, double x, double y,double vx, double vy);
void Euler (double tinicio,double tfin,int n);
void LF(double tinicio,double tfin,int n);
void RK(double tinicio,double tfin,int n);


int main () {
    Euler(0,1,1000);
    LF(0,1,10000);
    RK(0,2,1000);
        


        

    

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
    double g=39.478;//constante gravitacional en las unidades adecuadas
    double m=1;
    return -(g*m)*x/pow(sqrt((x*x+y*y)),3);
}
double funcion2y(double t, double x, double y,double vx, double vy)
{
    double g=39.478;
    double m=1;
    return -(g*m)*y/pow(sqrt((x*x+y*y)),3);
}



void Euler (double tinicio,double tfin,int n)
{
    
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
}




//
//
//
//

void LF(double tinicio,double tfin,int n)
{
    double dt=(tfin-tinicio)/n;

    double tlf[n];    
    double x_1lf[n];
    double x_2lf[n];
    double y_1lf[n];
    double y_2lf[n];
    
    double rlf[n];
    
        //Se toman las condiciones 
    tlf[0]=tinicio;
    tlf[1]=tinicio + dt;
    
    x_1lf[0]= 0.1163;
    y_1lf[0]= 0.9772;

    rlf[0]= sqrt(x_1lf[0]*x_1lf[0]+y_1lf[0]*y_1lf[0]);
    
    
    
    x_2lf[0]=-6.35;
    y_2lf[0]=0.606;
    
    x_1lf[1]= x_1lf[0]+dt*funcion1x(tlf[0], x_1lf[0], x_2lf[0]);
    y_1lf[1]= y_1lf[0]+dt*funcion1y(tlf[0], x_1lf[0], x_2lf[0]);
    
    x_2lf[1]= x_2lf[0]+dt*funcion2x(tlf[0],x_1lf[0],y_1lf[0],x_2lf[0],y_2lf[0]);
    y_2lf[1]= y_2lf[0]+dt*funcion2y(tlf[0],x_1lf[0],y_1lf[0],x_2lf[0],y_2lf[0]);


    
    ofstream leapfrog;
    leapfrog.open ("OrbitaLF.txt");
    for (int i=2;i<n;i++){
        tlf[i] = tlf[i-1] + dt;

        double x_prima_1 = funcion1x(tlf[i-1],x_1lf[i-1],x_2lf[i-1]);
        double y_prima_1 = funcion1y(tlf[i-1],y_1lf[i-1],y_2lf[i-1]);
            
            
  
        x_1lf[i] = x_1lf[i-2] + 2*dt*x_prima_1;
        y_1lf[i] = y_1lf[i-2] + 2*dt*y_prima_1;
        
        

        double x_prima_2 = funcion2x(tlf[i-1],x_1lf[i-1],y_1lf[i-1],x_2lf[i-1],y_2lf[i-1]);
        double y_prima_2 = funcion2y(tlf[i-1],x_1lf[i-1],y_1lf[i-1],x_2lf[i-1],y_2lf[i-1]);
            
 
        x_2lf[i] = x_2lf[i-2] + 2*dt*x_prima_2;  
        y_2lf[i] = y_2lf[i-2] + 2*dt*y_prima_2;

        
        rlf[i]=sqrt(x_1lf[i]*x_1lf[i]+y_1lf[i]*y_1lf[i]);
        leapfrog <<tlf[i]<< " " << x_1lf[i] << " " << y_1lf[i] << " " << x_2lf[i]<< " " << y_2lf[i] << " " << rlf[i] <<"\n";
    }
}




void RK(double tinicio,double tfin,int n)
{
    
        double dt=(tfin-tinicio)/n;

        double t[n];
    
    
        double x_1[n];
        double x_2[n];
        double y_1[n];
        double y_2[n];
    
        double r[n];
        
    ofstream kutta;
    kutta.open ("OrbitaRK.txt");
    
    x_1[0]= 0.1163;
    y_1[0]= 0.9772;
    r[0]= sqrt(x_1[0]*x_1[0]+y_1[0]*y_1[0]);
    
    
    x_2[0]=-6.35;
    y_2[0]=0.606;
    
       
    
    
        
    for(int i=1;i<n;i++)
    {
        

        
        
        double k1_1x = funcion1x(t[i-1],x_1[i-1],x_2[i-1]);
        double k1_1y = funcion1y(t[i-1],y_1[i-1],y_2[i-1]);
        double k1_2x = funcion2x(t[i-1],x_1[i-1],y_1[i-1],x_2[i-1],y_2[i-1]);
        double k1_2y = funcion2y(t[i-1],x_1[i-1],y_1[i-1],x_2[i-1],y_2[i-1]);

        double t1 = t[i-1]+(dt/2);
        double x1_1 = x_1[i-1]+(dt/2)*k1_1x;
        double y1_1 = y_1[i-1]+(dt/2)*k1_1y;
        double x1_2 = x_2[i-1]+(dt/2)*k1_2x;
        double y1_2 = y_2[i-1]+(dt/2)*k1_2y;

        

        
        double k2_1x = funcion1x(t1,x1_1,x1_2);
        double k2_1y = funcion1y(t1,y1_1,y1_2);
        double k2_2x = funcion2x(t1,x1_1,y1_1,x1_2,y1_2);
        double k2_2y = funcion2y(t1,x1_1,y1_1,x1_2,y1_2);

        

        
        double t2 = t[i-1]+(dt/2);
        double x2_1 = x_1[i-1]+(dt/2)*k2_1x;
        double y2_1 = y_1[i-1]+(dt/2)*k2_1y;
        double x2_2 = x_2[i-1]+(dt/2)*k2_2x;
        double y2_2 = y_2[i-1]+(dt/2)*k2_2y;
        
        
        double k3_1x = funcion1x(t2,x2_1,x2_2);
        double k3_1y = funcion1y(t2,y2_1,y2_2);
        double k3_2x = funcion2x(t2,x2_1,y2_1,x2_2,y2_2);
        double k3_2y = funcion2y(t2,x2_1,y2_1,x2_2,y2_2);

        

        
        double t3 = t[i-1]+dt;
        double x3_1 = x_1[i-1]+dt*k3_1x;
        double y3_1 = y_1[i-1]+dt*k3_1y;
        double x3_2 = x_2[i-1]+dt*k3_2x;
        double y3_2 = y_2[i-1]+dt*k3_2y;
        
        
        
        double k4_1x = funcion1x(t3,x3_1,x3_2);
        double k4_1y = funcion1y(t3,y3_1,y3_2);
        double k4_2x = funcion2x(t3,x3_1,y3_1,x3_2,y3_2);
        double k4_2y = funcion2y(t3,x3_1,y3_1,x3_2,y3_2);
        
        double k1promx = (1.0/6.0)*(k1_1x + 2.0*k2_1x + 2.0*k3_1x + k4_1x);
        double k2promx = (1.0/6.0)*(k1_2x + 2.0*k2_2x + 2.0*k3_2x + k4_2x);
        
        double k1promy = (1.0/6.0)*(k1_1y + 2.0*k2_1y + 2.0*k3_1y + k4_1y);
        double k2promy = (1.0/6.0)*(k1_2y + 2.0*k2_2y + 2.0*k3_2y + k4_2y);
         
        
        t[i]=t[i-1]+dt;
        
        x_1[i]=x_1[i-1]+dt*k1promx;
        y_1[i]=y_1[i-1]+dt*k1promy;
            
        x_2[i]=x_2[i-1]+dt*k2promx;
        y_2[i]=y_2[i-1]+dt*k2promy;
        
        kutta <<t[i]<< " " << x_1[i] << " " << y_1[i] << " " << x_2[i]<< " " << y_2[i] << " " <<"\n";

    }
}
