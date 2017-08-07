#include <iostream>
using namespace std;

/*
Storage class
-------------------
A storage class defines the scope (visibility) and life-time of variables and/or functions within a C++ Program. These specifiers precede the type that they modify. There are following storage classes, which can be used in a C++ Program
    auto :
        default storage class for all local variables
    register :
        define local variables that should be stored in a register instead of RAM. This means that the variable has a maximum size equal to the register size (usually one word) and can't have the unary '&' operator applied to it (as it does not have a memory location).
    static :
        Instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating and destroying it each time it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.
        Can be applied to global variables. When this is done, it causes that variable's scope to be restricted to the file in which it is declared.
        In C++, when static is used on a class data member, it causes only one copy of that member to be shared by all objects of its class.
    extern :
        used to give a reference of a global variable that is visible to ALL the program files. When you use 'extern' the variable cannot be initialized as all it does is point the variable name at a storage location that has been previously defined.
        When you have multiple files and you define a global variable or function, which will be used in other files also, then extern will be used in another file to give reference of defined variable or function. Just for understanding extern is used to declare a global variable or function in another file.
        most commonly used when there are two or more files sharing the same global variables or functions as explained below.

    mutable :
        allows a member of an object to override constness. That is, a mutable member can be modified by a const member function.
*/


// Function declaration
void func(void);
void func2(void);

static int count = 10; /* Global variable */

int main()
{
   while(count--)
   {
      func();
      func2();
   }
   return 0;
}

// Function definition
void func( void )
{
   static int i = 5; // local static variable
   i++;
   std::cout << "i is " << i ;
   std::cout << " and count is " << count << std::endl;
}

void func2(void)
{
  cout<<"In func2: count is "<<count<<endl;
  //cout<<"In func2: i is "<<i<<endl;  //i can't be identified from the variable in the func
}
