## link: https://binarysearch.com/problems/Word-Formation
## Difficulty: Easy
## First Attempt: Yes
## Topics: String, Hashtable
"""
First create a count hashmap for letters
then for each word create a count hashmap
    then for each count if word-hashmap check if the same or higher value is present in
    letters's hashmap

"""

class Solution:
    def solve(self, words, letters):
        
        longest = 0
        lc = {}
        for l in letters:
            if l in lc:
                lc[l] += 1
            else:
                lc[l] = 1


        for word in words:
            wc = {}
            possible = True
            for w in word:
                if w in wc:
                    wc[w] += 1
                else:
                    wc[w] = 1

            for w in wc:
                if w in lc and lc[w] >= wc[w]:
                    continue
                else:
                    possible = False
                    break
            
            ## word possible
            if possible:
                longest = max(len(word), longest)

        return longest

