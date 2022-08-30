#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        counter = 0
        output = []
        for num in nums:
            if target == num:
                output.append(counter)
                try:
                    while nums[counter+1] == target:
                        counter += 1
                    output.append(counter)
                    return output
                except Exception as e:
                    output.append(counter)
                    return output
            else:
                counter += 1
                
        return output