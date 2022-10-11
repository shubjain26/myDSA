"""
Problem Statement:
Given a stream of integers return median at any time.

Company: Bosch
Date: 11 Oct 2022

Time Complexity: 
    Insertion: O(Log(n))
    Median: O(1)

Space Complexity: O(n)

Approach:
    Maintain a sorted list. 
    Apply binary search for insetion of element

Difficulty: Medium
Topic: Binary Search
"""


class MedianStream:
    """Class to get median of a stream of numbers."""

    def __init__(self):
        self.list = []

    def add_number(self, num: float) -> None:
        """Adds number to stream

        Args:
            num (float): Input float number
        """
        if len(self.list) == 0:
            self.list.append(num)
        else:
            ind = self.find_index(num)  # binary search
            # print("returned ind", ind)
            self.list = self.list[:ind] + [num] + self.list[ind:]

        return

    def get_median(self) -> float:
        """Returns median of stream

        Returns:
            float: Median value
        """
        if len(self.list) == 0:
            return 0

        mid = int(len(self.list) / 2)
        print("mid: ", mid)
        if len(self.list) % 2 == 0:
            return (self.list[mid - 1] + self.list[mid]) / 2
        else:
            return self.list[mid]

    def find_index(self, num):
        """Finds the index where element needs to be inserted"""
        if num > self.list[-1]:
            return len(self.list)

        elif num < self.list[0]:
            return 0

        ## Linear Search O(n)
        # for i in range(len(self.list)-1):
        #     if num >= self.list[i] and num < self.list[i+1]:
        #         return i+1

        ## Binary Search O(log(n))
        l, r = 0, len(self.list) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if num >= self.list[mid] and num < self.list[mid + 1]:
                return mid + 1
            else:
                if num > self.list[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return len(self.list) + 1


if __name__ == "__main__":
    median_stream = MedianStream()
    param_2 = median_stream.get_median()
    for num in [10, 22, 3, 0, 0, -1]:
        median_stream.add_number(num)

    median = median_stream.get_median()
    print(median_stream.list)
    print(median)
