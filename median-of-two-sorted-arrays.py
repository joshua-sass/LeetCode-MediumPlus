import math
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if nums1 == []:
            return statistics.median(nums2)
        if nums2 == []:
            return statistics.median(nums1)
        
        if (len(nums1)+len(nums2))%2 == 1:
            med_flag = False
            med_val = ceil((len(nums1)+len(nums2))/2)
        else:
            med_flag = True
            med_val = (len(nums1)+len(nums2))/2
        
        one_iterator = 0
        two_iterator = 0
        iterator = 0
        current_val = 0
        
        if len(nums1) > len(nums2):
            padding_num = max(nums1[-1], nums2[-1])
            padding_arr = [padding_num for x in range(len(nums1)-len(nums2))]
            for val in padding_arr:
                nums2.append(val)
        elif len(nums2) > len(nums1):    
            padding_num = max(nums1[-1], nums2[-1])
            padding_arr = [padding_num for x in range(len(nums2)-len(nums1))]
            for val in padding_arr:
                nums1.append(val)        
        
        while iterator != med_val:
            if  nums1[one_iterator] > nums2[two_iterator]:
                current_val = nums2[two_iterator]
                two_iterator += 1
            else:
                current_val = nums1[one_iterator]
                one_iterator += 1
            iterator += 1
            
        if med_flag == True and two_iterator < len(nums2) and one_iterator < len(nums1):
            return (current_val + min(nums1[one_iterator], nums2[two_iterator]))/2
        elif med_flag == True:
            if two_iterator >= len(nums2):
                return (current_val + nums1[one_iterator])/2
            else:
                return (current_val + nums2[two_iterator])/2
        return current_val