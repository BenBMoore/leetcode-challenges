import argparse
from typing import List


class Solution:
    def count_elements(self, arr: List[int]) -> int:
        numbers_count = {}
        duplicates = 0
        for x in arr:
            if x in numbers_count:
                numbers_count[x] += 1
            else:
                numbers_count[x] = 1
        for key, value in numbers_count.items():
            if key + 1 in numbers_count:
                duplicates += value
        return duplicates


def main():
    parser = argparse.ArgumentParser(description='Process a list of ints.')
    parser.add_argument('ints', metavar='N', type=int, nargs='+',
                        help='Enter multiple ints')

    args = parser.parse_args()
    numbers = args.ints
    max_sum = Solution().group_anagrams(numbers)

    print(max_sum)


if __name__ == "__main__":
    main()
