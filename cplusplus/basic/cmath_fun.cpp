#include <iostream>
#include <cmath>
using namespace std;

/*
S.N.  Function & Purpose
1  double cos(double);
   This function takes an angle (as a double) and returns the cosine.
2  double sin(double);
   This function takes an angle (as a double) and returns the sine.
3  double tan(double);
   This function takes an angle (as a double) and returns the tangent.
4  double log(double);
   This function takes a number and returns the natural log of that number.
5  double pow(double, double);
   The first is a number you wish to raise and the second is the power you wish to raise it t
6  double hypot(double, double);
   If you pass this function the length of two sides of a right triangle, it will return you the length of the hypotenuse.
7  double sqrt(double);
   You pass this function a number and it gives you this square root.
8  int abs(int);
   This function returns the absolute value of an integer that is passed to it.
9  double fabs(double);
   This function returns the absolute value of any decimal number passed to it.
10 double floor(double);
   Finds the integer which is less than or equal to the argument passed to it.
*/
int main ()
{
   // number definition:
   short  s = 10;
   int    i = -1000;
   long   l = 100000;
   float  f = 230.47;
   double d = 200.374;

   // mathematical operations;
   cout << "sin(90) :" << sin(90) << endl;
   cout << "cos(90) :" << cos(90) << endl;
   cout << "abs(-100.20)  :" << abs(-100.20) << endl;
   cout << "fabs(-100.20)  :" << fabs(-100.20) << endl;
   cout << "floor(d) :" << floor(d) << endl;
   cout << "sqrt(16) :" << sqrt(16) << endl;
   cout << "pow(2, 4) :" << pow(2,4) << endl;

   return 0;
}
