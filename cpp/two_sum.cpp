#include <vector>
#include <unordered_map>

class Solution {
 public:
  std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> numToIndex;

    for (int i = 0; i < nums.size(); ++i) {
      if (numToIndex.count(target - nums[i]))
        return {numToIndex[target - nums[i]], i};
      numToIndex[nums[i]] = i;
    }

    throw;
  }
};
