## link: https://binarysearch.com/problems/Maximum-Number-by-Inserting-Five
## Difficulty: Easy
## First Attempt: No
## Topics: array

"""
By analysing the patterm for positive and negative numbers

for positive numbers, 5 should be inserted just before a digit < 5
for negative numbers, 5 should be inserted just before a digit > 5


num : 923   -> ans : 9523
num : 234   -> ans : 5234

num: -234   -> ans: -2345
num: -236   -> ans: -2356
"""


class Solution:
    def solve(self, n):

        if n == 0:
            return 50
        if n > 0:
            is_positive = True
            str_n = str(n)
        else:
            is_positive = False
            str_n = str(n * (-1))

        if is_positive:
            pos = -1
            for i, digit in enumerate(str_n):
                print(i, digit)
                if int(digit) < 5:
                    pos = i
                    break

            if pos != -1:
                new_num_str = str_n[:pos] + "5" + str_n[pos:]
                new_num = int(new_num_str)

            else:
                new_num_str = str_n + "5"
                new_num = int(new_num_str)

        else:
            pos = -1
            for i, digit in enumerate(str_n):
                print(i, digit)
                if int(digit) > 5:
                    pos = i
                    break

            if pos != -1:
                new_num_str = str_n[:pos] + "5" + str_n[pos:]
                new_num = int(new_num_str)

            else:
                new_num_str = str_n + "5"
                new_num = int(new_num_str)

            new_num = new_num * (-1)

        return new_num
