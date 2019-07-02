#include <iostream>
#include <array>
using namespace std;
float prod(float,float);
int main(){
   int * p;
   p=prod();
   int arr1[5] = {1,2,3,4,5};
   int arr2[5] = {10,20,30,40,50};
   for ( int i = 0; i < 5; i++ ) {
       cout << *(p + i) << endl;
   }
   return 0;
}

float * prod(){

   
   int arr1[]={1,2,3,4,5};
   int arr2[]={10,20,30,40,50};

   float prod[5];
   for(int i=0; i<5;i++){
     prod[i]=arr1[i]*arr2[i];
   }
   
    return prod;
}