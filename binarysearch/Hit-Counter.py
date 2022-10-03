## link: https://binarysearch.com/problems/Hit-Counter
## Difficulty: Medium
## First Attempt: No
## Topics: Data Structure

"""
Approach 1: Brute-Force
    - store the hits timestamp in a list
    - to get hit count for TS, just iterate through each of them and check if they are > TS-60

Approach 2: Using binary search     -> FAILED
    - store the hits timestamp in a list
    - Use binary search to find any hit > TS-6
    - Once any hit is found, slide left and right to find all hits > TS-60 and hits < TS

Approach 3: 
    - keep a hashmap to keep count of hits for each timestamp
    - keep a list to store last 60 timestamps
    - in the list store the timestamp at a particular index, 
        index = timestamp % 61 (61 because 0 and 60 both should be stored)
        value = timestamp
    - to count number of hits, just iterate on all 61 values in hits list to find all hits > TS-60 and hits < TS
"""
# APPROACH 3: Fastest
class HitCounter:
    def __init__(self):
        self.hits_count = {}
        self.hits = [-100]*61

    def add(self, timestamp):
        self.hits[timestamp%61] = timestamp
        if timestamp in self.hits_count:
            self.hits_count[timestamp] += 1
        else:
            self.hits_count[timestamp] = 1
            

    def count(self, timestamp):
        ct = 0
        for ts in self.hits:
            if ts >= timestamp-60:
                ct += self.hits_count[ts] 

        return ct





# APPROACH 2:
"""
class HitCounter:
    def __init__(self):
        self.hits_ts = []
        self.total_count = 0
        self.ts_index = {}

    def add(self, timestamp):
        self.hits_ts.append(timestamp)
        self.ts_index[timestamp] = self.total_count
        self.total_count += 1

    def count(self, timestamp):

        count = 0
        ts_min = timestamp - 60
        ts_max = timestamp

        nearby_index = self.binary_search(timestamp, ts_min, ts_max)
        print("nearby_index",nearby_index)
        if nearby_index >= 0:
            count = self.count_near_index(nearby_index, ts_min, ts_max)
        print("count",count)

        # for hit in self.hits_ts:
        #     if hit >= ts_min and hit <=ts_max:
        #         hits_count += 1

        return count

    def count_near_index(self, index, ts_min, ts_max):
        left_ptr = index
        right_ptr = index

        while True:
            if (left_ptr-1 >= 0) and  (self.hits_ts[left_ptr-1] >= ts_min):
                left_ptr -= 1
            else:
                break
        while True:
            if (right_ptr+1 < len(self.hits_ts)) and (self.hits_ts[right_ptr]+1 <= ts_max):
                right_ptr += 1
            else:
                break

        count = right_ptr - left_ptr + 1
        return count

    def binary_search(self, timestamp, ts_min, ts_max):

        if len(self.hits_ts) == 1 and self.hits_ts[0] >= ts_min and self.hits_ts[0] <= ts_max :
            return 0
        start = 0
        end = len(self.hits_ts)-1
        while start < end :
            mid = int((start+end)/2)
            hit = self.hits_ts[mid]
            print("self.hits_ts,start,end,mid,hit,ts_min, ts_max",self.hits_ts,start,end,mid,hit,ts_min, ts_max)
            if hit >= ts_min and hit <= ts_max:
                return mid
            
            elif hit > ts_max:
                end = mid-1
                continue
            elif hit < ts_min:
                start = mid+1
                continue
            else:
                print("unexpected condition. hit, ts_min, ts_max",hit, ts_min, ts_max)
            
            print("start,end",start,end)

        return -1
"""
