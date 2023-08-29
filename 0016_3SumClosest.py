from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        index = 0 
        nums.sort()
        result = 0
        least_distance = abs(nums[index] + nums[index+1] + nums[index+2] - target)
        result = nums[index] + nums[index+1] + nums[index+2]
        for i in range(len(nums)-2):
            i2, i3 = i+1, len(nums)-1 
            while i2 < i3:
                sum = nums[i] + nums[i2] + nums[i3]
                if abs(sum - target) < least_distance: 
                    least_distance = abs(sum - target) 
                    result = sum 
                if sum < target : 
                    i2 +=1       
                else :
                    i3 -=1    
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2))