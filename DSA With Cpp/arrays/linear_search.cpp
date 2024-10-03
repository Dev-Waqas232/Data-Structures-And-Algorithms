// For searching an element in an array but with time complexity of O(n)
#include <iostream>
using namespace std;

int linearSearch(int arr[], int target, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == target)
        {
            return i;
        }
    }

    return -1;
}

int main()
{
    int arr[] = {4, 2, 7, 8, 1, 2, 5};
    int target = 9;
    int ans = linearSearch(arr, target, 7);
    cout << ans;
}