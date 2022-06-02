// C++ program to demonstrate the use of std::min
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    // [REQ-001]
    int a = 5;
    int b = 7;
    // [/REQ-001]
    cout << std::min(a, b) << "\n";
 
    // Returns the first one if both the numbers
    // are same
    cout << std::min(7, 7);
 
    return 0;
}