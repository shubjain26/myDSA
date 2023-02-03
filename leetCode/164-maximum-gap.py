"""
Ref: https://leetcode.com/problems/maximum-gap/

Difficulty: Hard

Topic: Array, Sort, Bucket Sort, Radix Sort

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
    The minimum value of the answer can be when all the elements are evenly spaced.
    When this happens, the maximum gap (answer) will be : (Max - Min) // len(array) - 1

    Create buckets of this size : (max - min) // (len(array) - 1)

    Iterate through the items of the list, find the bucket where it fits
    Store min and max of each bucket, now the answer will be only between buckets
    Maximum Gap can be (across the bucket only) ,say B2.min - B1.max
        example : B1[min,max]...B2[min,max]...B3[min,max]...B4[min,max]...B4[min,max]
"""


from collections import defaultdict


class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        arr_min = min(nums)
        arr_max = max(nums)
        n = len(nums)

        if n < 2:
            return 0

        bucket_size = max(1, (arr_max - arr_min) // (n - 1))

        buckets = defaultdict(list)

        for num in nums:
            key = (num - arr_min) // bucket_size
            if not buckets[key]:
                buckets[key] = [num, num]
            else:
                buckets[key] = [min(buckets[key][0], num), max(buckets[key][1], num)]

        prekey = -1
        max_gap = 0
        for key in sorted(buckets.keys()):
            if prekey != -1:
                max_gap = max(buckets[key][0] - buckets[prekey][1], max_gap)

            prekey = key

        return max_gap
