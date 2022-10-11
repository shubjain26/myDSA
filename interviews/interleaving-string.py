"""
TODO
ref: https://leetcode.com/problems/interleaving-string/


Interview: Arzoo
Date : 10-Oct-2022
Difficulty : Medium

Topic: Dynamic Programming
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1_ptr = 0
        l2_ptr = 0
        matched = ""
        
        result = True
        for c in s3:
            print(f"comparing : {c}, with s1[{l1_ptr}]: {s1[l1_ptr]}, s2[{l2_ptr}]: {s2[l2_ptr]}")
            

            if l1_ptr < len(s1) and c == s1[l1_ptr]:
                print("inc l1")
                l1_ptr += 1
            elif l2_ptr < len(s2) and c == s2[l2_ptr]:
                print("inc l2")
                l2_ptr += 1
            else:
                print("exiting ...")
                print(l1_ptr,l2_ptr)
                result = False
                break

            matched += c
            print(matched)

        return result