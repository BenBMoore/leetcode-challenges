import argparse
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        # Define max if no summing takes place.
        max_sum, curr_sum = max(nums), 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum


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
