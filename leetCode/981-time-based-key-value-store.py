"""
Ref: https://leetcode.com/problems/time-based-key-value-store/

- Hash table, Design, Binary Search

Approach 
"""

class TimeMap:

    def __init__(self):
        self.store = {}
        self.timestamps = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        
        
        if key in self.store:
            if not timestamp in self.timestamps[key]:
                self.timestamps[key].append(timestamp)
            self.store[key][timestamp] = value

        else:
            self.store[key] = {timestamp : value}
            self.timestamps[key] = [timestamp]


    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            else:
                # ts_index = self.binary_search(self.timestamps[key], timestamp)
                
                l = 0 
                r = len(self.timestamps[key]) -1
                res = -1
                while l <= r:
                    mid = (l+r) // 2
                    if self.timestamps[key][mid] <= timestamp:
                        res = mid
                        l = mid + 1
                    else:
                        r = mid - 1
                
                # print(ts_index, self.timestamps[key], timestamp)
                if res == -1 :
                    return ""
                ts = self.timestamps[key][res]
                return self.store[key][ts]

        else:
            return ""
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)