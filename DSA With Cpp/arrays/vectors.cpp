// Vectors are used for dynamic sized array
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // Declaring Vector
    vector<int> vec1;             // it is of size 0 initially as there is no element in the vector
    vector<int> vec2 = {1, 2, 3}; // it is of the same size as the number of elements on right side initially
    vector<int> vec3(3, 0);       // first value is the size of vector, second value is the value of every index initially

    // For Each Loop in vectors
    for (int num : vec3)
    {
        cout << num << endl;
    }

    // Useful functions of vector
    // 1. Size of vector
    cout << "Size of vector is " << vec3.size() << endl;
    // 2. Adding element in the last of a vector
    vec3.push_back(23);
    cout << "Size of vector after push_back() " << vec3.size() << endl;
    // 3. Removing element from end of a vector
    vec3.pop_back();
    cout << "Size of vector after pop_back() " << vec3.size() << endl;
    // 4. getting first value of vector
    cout << vec3.front() << endl;
    // 5. getting last value of vector
    cout << vec3.back() << endl;
    // 6. accessing the value at a particular index
    cout << vec3.at(1) << endl;
}