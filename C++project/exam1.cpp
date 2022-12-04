// #include <iostream>
// using namespace std;
 
// // Function to find factorial
// // of given number
// unsigned int factorial(unsigned int n)
// {
//     if (n == 0 || n == 1)
//         return 1;
//     return n * factorial(n - 1);
// }
 
// // Driver code
// int main()
// {
//     int num = 5;
//     cout << "Factorial of "
//          << num << " is " << factorial(num) << endl;
//     return 0;
// }

// # include<iostream>

// using namespace std;

// void my_swap(double& x, double &y)

// {

//   double temp=x;

//   x=y;

//   y=temp;

// }

// int main (){

//   double a = 5.5, b=6.6;

//   cout << " Numbers after swapping \n";

//   cout << "a = "<<a<< "b = "<<b;

//   my_swap(a,b);

//   cout<<"\n\nNumbers after swapping \n";

//   cout<<"a = "<<a<<" b = "<<b;

// }

#include <iostream>//delete semicolon

using namespace std;//add semicolon
int min(int a[], int size);//add semi colon 

  int main() 
  { 
      int a[] = {3, 2, 1, 6, 5, 7}; //remove []a and add a[] in Array declaration 
       int size = sizeof(a)/ sizeof(a[0]);//this code is used to find out the size of array
     cout<<"The minimum value in array a is:"<<min(a,size);//syntax:cout << "Some String";
      //System("pause"); 
      return 0; 
          
      } 
      int min(int a[], int size)//delete semicolon 
     {
      int result = a[0];//remove (),add [] 
      for(int index = 1; index<size;index++)//remove index==1 and add idex=1
      {
      if(result>a[index])
      result=a[index];
      }
      return result;//add return statement
     }