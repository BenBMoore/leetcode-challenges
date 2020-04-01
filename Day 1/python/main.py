from collections import defaultdict
from typing import List


class Solution:       

    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        
        for x in nums:
            hash_table[x] += 1
        
        for x in hash_table:
            if hash_table[x] == 1:
                return x


def main():
    getSingleNumber = Solution().singleNumber([2,2,1])

    if getSingleNumber == 1: 
        print("Successful Test")
    else:
        print("Failed Test")

if __name__ == "__main__":
    main()