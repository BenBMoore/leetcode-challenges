import argparse


class Solution:

    def is_happy(self, n: int) -> bool:
        answer = n
        seen_answers = {}

        while answer != 1:
            # Separate int into its component parts, square the number, and sum
            answer = sum([pow(int(x), 2) for x in str(answer)])

            if answer in seen_answers:
                return False
            else:
                seen_answers[answer] = 1
        return True


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integer', metavar='N', type=int, nargs=1,
                        help='An integer for processing by the happy number process')

    args = parser.parse_args()
    number = args.integer[0]
    happy = Solution().is_happy(number)

    if happy:
        print("Number is happy")
    else:
        print("Number is sad")


if __name__ == "__main__":
    main()
