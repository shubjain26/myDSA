"""
Ref: https://leetcode.com/problems/3sum/

- Topics: Array , two pointer

Time Complexity: O(n.logn)
Space Complexity : O(1)

Approach: 
    - Sort the array.
    - Select one element and solve for two elements using two sum using two pointer.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        sn = nums

        triplets = []
        # hashes = {}

        for i in range(len(sn)):

            if i > 0 and sn[i] == sn[i - 1]:
                continue
            t = -1 * sn[i]

            l = i + 1
            r = len(sn) - 1

            while l < r:
                if (l > i + 1) and sn[l] == sn[l - 1]:
                    l += 1
                    continue
                if (r < len(sn) - 1) and sn[r] == sn[r + 1]:
                    r -= 1
                    continue

                cs = sn[l] + sn[r]
                if cs == t:
                    rs = [sn[i], sn[l], sn[r]]

                    triplets.append([sn[i], sn[l], sn[r]])

                    # hs = tuple(rs)
                    # if not hs in hashes:
                    #     triplets.append([sn[i], sn[l], sn[r]])
                    #     hashes[hs] = 1
                    l += 1
                elif cs > t:
                    # while sn[r] == sn[r-1]:
                    r -= 1

                else:
                    # while sn[l] == sn[l+1] :
                    l += 1

        return triplets
