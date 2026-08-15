#include<bits/stdc++.h>
using namespace std;

void rotate(vector<int> &nums, int n){

    int temp = nums[0];
    for(int i=1; i < n; i++)
    {
        nums[i -1 ] = nums[i];
    }
    nums[n - 1] = temp;

    for(int i : nums){
        cout << i << " ";
    }

}

int main(){

    vector<int> nums;
    nums = {1, 2, 3, 4, 5};

    int n = nums.size();

    rotate(nums, n);


    return 0;
}