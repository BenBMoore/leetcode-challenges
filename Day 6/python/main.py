import argparse
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        # Will hold data as sorted : [str anagrams]
        anagrams = dict()
        str_sorted = ["".join(sorted(x)) for x in strs]

        for index, value in enumerate(str_sorted):
            if value in anagrams:
                anagrams[value].append(strs[index])
            else:
                anagrams[value] = [strs[index]]

        return [anagrams[x] for x in anagrams]


def main():
    parser = argparse.ArgumentParser(description='Process a list of strings.')
    parser.add_argument('strings', metavar='N', type=str, nargs='+',
                        help='Separate strings to process')

    args = parser.parse_args()
    strs = args.strings
    max_sum = Solution().group_anagrams(strs)

    print(max_sum)


if __name__ == "__main__":
    main()
