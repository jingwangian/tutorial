/*
In C++, I/O is a sequence of bytes, called a stream, from the source to the
destination.The bytes are usually characters, unless the program requires other
types of information, such as a graphic image or digital speech. Therefore, a
stream is a sequence of characters from the source to the destination. There are
two types of streams:
Input stream: A sequence of characters from an input device to the computer.
Output stream: A sequence of characters from the computer to an output device.

To receive data from the keyboard and send to the screen, every C++ program must
use the header file iostream .This head file contains the definitions of two data
types,istream (input stream) and ostream (output stream). The header file also con-
tains two variable declarations, one for cin (pronounced ‘‘see-in’’), which stands
for common input, and one for cout (pronounced ‘‘see-out’’), which stands for
common output.
Variables of type istream are called input stream variables;  e.x: cin
variables of type ostream are called output stream variables. e.x: cout
>> extraction operator
*/
#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

void setw_fn()
{
   int n[ 10 ]; // n is an array of 10 integers

   // initialize elements of array n to 0
   for ( int i = 0; i < 10; i++ ) {
      n[ i ] = i + 100; // set element at location i to i + 100
   }

   cout << "Element" << setw( 13 ) << "Value" << endl;

   // output each array element's value
   for ( int j = 0; j < 10; j++ ) {
      cout << setw( 7 )<< j << setw( 13 ) << n[ j ] << endl;
   }
}

void cin_input()
{
   int int_a;
   int int_b;
   char char_a;
   double double_a;


   cin>>int_a>>char_a>>double_a;
   cout<<int_a<<endl;
   cout<<char_a<<endl;
   cout<<double_a<<endl;
   cout<<"hhh"<<endl;
   cin>>int_b;
   cout<<"Please input number for int_b"<<endl;
   cout<<int_b<<endl;
   cout<<"Exit cin_input"<<endl;
}

/*
cin.get(var_char) is used to get one char variable from the input and
put it in the variable.
*/
void cin_get()
{
   char ch1, ch2;
   int num;

   cin.get(ch1);
   cin.get(ch2);
   cin >> num;

   // input A 25
   // output ch1='A' ch2='' num=25


   //Get same result using following statements
   cin >> ch1;
   cin.get(ch2);
   cin >> num;


}

/*
cin.ignore(intExp, chExp);
intExp : how many characters should be ignored
chExp: Stop ignore when encounter this
*/
void cin_ignore()
{

}
int main ()
{
   setw_fn();
   cin_input();

   return 0;
}
