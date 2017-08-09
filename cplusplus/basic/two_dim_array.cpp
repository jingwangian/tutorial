/*
Two-Dimensional Arrays
-------------------
type arrayName [ x ][ y ];

int a[3][4] = {
   {0, 1, 2, 3} ,   //  initializers for row indexed by 0
   {4, 5, 6, 7} ,   //  initializers for row indexed by 1
   {8, 9, 10, 11}   //  initializers for row indexed by 2
};

int a[0][4] = {
   {0, 1, 2, 3} ,   //  initializers for row indexed by 0
   {4, 5, 6, 7} ,   //  initializers for row indexed by 1
   {8, 9, 10, 11}   //  initializers for row indexed by 2
};
*/

#include <iostream>
using namespace std;


int main ()
{
    int i;
    static int a[][] = {
     {0, 1, 2, 3} ,   /*  initializers for row indexed by 0 */
     {4, 5, 6, 7} ,   /*  initializers for row indexed by 1 */
     {8, 9, 10, 11}   /*  initializers for row indexed by 2 */
    };

    cout<<"address of a is"<<a<<endl;

    cout<<"sizeof(a)"<<sizeof(a)<<endl;
    cout<<"sizeof(a[0])"<<sizeof(a[0])<<endl;
    cout<<"sizeof(a[0][0])"<<sizeof(a[0][0])<<endl;
}

