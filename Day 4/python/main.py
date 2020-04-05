import argparse
from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in reversed(range(0, len(nums))):
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
            

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='An integer for processing by the happy number process')

    args = parser.parse_args()
    number = args.integers
    max_sum = Solution().max_sub_array(number)

    print(max_sum)


if __name__ == "__main__":
    main()
