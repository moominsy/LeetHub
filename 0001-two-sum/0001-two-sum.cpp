class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v(2);
        std::cout << nums.size() << std::endl;
        for(int i=0; i<nums.size(); i++){
            for(int j=0; j<nums.size(); j++){
                if(nums[i]+nums[j] == target && i!=j){
                    v[0]=i;
                    v[1]=j;
                    return v;
                }
            }
        }
    return v;
    }
};