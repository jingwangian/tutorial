#include <iostream>
using namespace std;

/*
variable define:
------------------------
    A variable definition means to tell the compiler where and how much to create the storage for the variable. A variable definition specifies a data type, and contains a list of one or more variables of that type as follows

    type variable_list;

variable declaration:
------------------------
    A variable declaration provides assurance to the compiler that there is one variable existing with the given type and name so that compiler proceed for further compilation without needing complete detail about the variable.

    A variable declaration is useful when you are using multiple files and you define your variable in one of the files which will be available at the time of linking of the program.

    You will use extern keyword to declare a variable at any place. Though you can declare a variable multiple times in your C++ program, but it can be defined only once in a file, a function or a block of code.

    // Variable declaration:
    extern int a, b;
    extern int c;
    extern float f;


Lvalue and Rvalue:
------------------------
    lvalue − Expressions that refer to a memory location is called "lvalue" expression. An lvalue may appear as either the left-hand or right-hand side of an assignment.

    rvalue − The term rvalue refers to a data value that is stored at some address in memory. An rvalue is an expression that cannot have a value assigned to it which means an rvalue may appear on the right- but not left-hand side of an assignment.

Local Variables
------------------------
    Variables that are declared inside a function or block are local variables. They can be used only by statements that are inside that function or block of code. Local variables are not known to functions outside their own.

Global Variables
------------------------
    Global variables are defined outside of all the functions, usually on top of the program. The global variables will hold their value throughout the life-time of your program.

    A global variable can be accessed by any function. That is, a global variable is available for use throughout your entire program after its declaration

Initializing Local and Global Variables
------------------------
    When a local variable is defined, it is not initialized by the system, you must initialize it yourself. Global variables are initialized automatically by the system when you define them as follows:

    Data Type   Initializer
    int             0
    char            '\0'
    float           0
    double          0
    pointer         NULL
*/

// Global variable declaration:
int g;

int main () {
   // Local variable declaration:
   int a, b;
   int c;

   // actual initialization
   a = 10;
   b = 20;
   c = a + b;

   cout << c;

   return 0;
}
