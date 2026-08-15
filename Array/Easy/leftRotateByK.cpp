#include<bits/stdc++.h>
using namespace std;

void Brute(vector<int> &nums, int n, int k){

    k = k % n;

    int temp[k];
    for(int i = 0; i < k; i++){
        temp[i] = nums[i];    
    }
    
    for(int i = k; i < n; i++){
        nums[i - k] = nums[i];
    }
    int j=0;
    for(int i = n - k; i < n; i++){
        nums[i] = temp[j];
        j++;
    }

    for(int i = 0; i < n; i++){
        cout << nums[i] << " ";
    }

}

void Better(vector<int> &nums, int n, int k){

    k = k % n;

    int temp[k];
    for(int i = 0; i < k; i++){
        temp[i] = nums[i];    
    }
    
    for(int i = k; i < n; i++){
        nums[i - k] = nums[i];
    }

    for(int i = n - k; i < n; i++){
        nums[i] = temp[i - (n-k)];
    }

    for(int i = 0; i < n; i++){
        cout << nums[i] << " ";
    }
}

void Optimal(vector<int> &nums, int n, int k){

    k = k % n;
    if(n == 0) return;

    reverse(nums.begin(), nums.end());
    reverse(nums.begin(), nums.begin()+k);
    reverse(nums.begin()+k, nums.end());

    for(int i = 0; i < n; i++){
        cout << nums[i] << " ";
    }
}

int main(){

    vector<int> nums;
    nums = {1, 2, 3, 4, 5, 6, 7};

    int n = nums.size();

    int k;
    cout<< "Enter the value of K : ";
    cin >> k;

    Optimal(nums, n, k);

    return 0;
}