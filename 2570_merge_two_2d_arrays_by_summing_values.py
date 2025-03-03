class Solution:
    def mergeArrays(self, nums1, nums2):
        
        
        # Keep track of left index (for nums1), right index (for nums2), and curr index (for adding entry to res)
        left = 0
        right = 0
        res = [] # result

        while left < len(nums1) and right < len(nums2):
            curr_left = nums1[left]
            curr_right = nums2[right]

            # Three Cases - if indices all the same, then add them together
            # If only one index matches curr_index, then set the number to that value
            # If no index matches curr_index, then add a [curr_index, 0] entry

            if curr_index == curr_left[0] == curr_right[0]:
                res.append([curr_index, curr_left[1] + curr_right[1]])
                left += 1
                right += 1

            elif curr_index == curr_left[0]:
                res.append(curr_left)
                left += 1

            elif curr_index == curr_right[0]:
                res.append(curr_right)
                right += 1

            curr_index += 1

        # Loop through remaining elements
        while left < len(nums1):
            res.append(nums1[left])
            left += 1
        
        while right < len(nums2):
            res.append(nums2[right])
            right += 1

        return res



# print(Solution().mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
# print(Solution().mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))