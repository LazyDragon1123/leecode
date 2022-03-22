from textwrap import indent


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sumlen = len(nums1) + len(nums2)
        targetind1 = sumlen // 2
        targetind2 = sumlen // 2 - 1
        ind1 = 0
        ind2 = 0
        ind = 0
        
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        print(targetind1+1)
        while ind != targetind1+1:
            if (nums1[ind1] >= nums2[ind2]):
                if ind == targetind2:
                    flag2 = 2
                    m21 = ind1
                    m22 = ind2
                if ind == targetind1:
                    flag1 = 2
                    m11 = ind1
                    m12 = ind2                    
                ind2 += 1
                ind +=1

            else:
                if ind == targetind2:
                    flag2 = 1
                    m21 = ind1
                    m22 = ind2                    
                if ind == targetind1:
                    flag1 = 1       
                    m11 = ind1
                    m12 = ind2                    
                ind1 += 1
                ind += 1        
            print(ind)
        # print(m11,m12,m21,m22)
        if sumlen %2 == 1:
            if flag1 == 1:
                return  nums1[m11]
            else:
                return nums2[m12]
        else:
            if (flag1 == 1) and (flag2==1):
                return (nums1[m11] + nums1[m21]) / 2
            elif (flag1 == 2) and (flag2==2):
                return (nums2[m12] + nums2[m22]) / 2
            elif (flag1 == 1) and (flag2==2):
                return (nums1[m11] + nums2[m22]) / 2
            elif (flag1 == 2) and (flag2==1):
                return (nums2[m12] + nums1[m21]) / 2            
            
            
# merge sort nlogn

# binary tree
