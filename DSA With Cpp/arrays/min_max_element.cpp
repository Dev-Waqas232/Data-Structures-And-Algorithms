// Find min and max element in the array
#include <iostream>
using namespace std;

int main()
{
    int arr[] = {5, 15, 22, 1, -15};
    int min = 0;
    int max = 0;

    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < size; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
        else if (arr[i] > max)
        {
            max = arr[i];
        }
    }

    cout << "Minimum number in the array is " << min << endl;
    cout << "Maximum number in the array is " << max << endl;
}