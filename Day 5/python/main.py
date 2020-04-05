import argparse
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        best_profit = 0
        for idx in range(0, len(prices) - 1):
            # If the price is not greater, then "sell at the peak", else buy/hold
            if prices[idx + 1] > prices[idx]:
                best_profit += prices[idx + 1] - prices[idx]
        return best_profit


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
