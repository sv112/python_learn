from math import floor, ceil


def check_if_palindrome(s, centre):

    sub_s = s[:centre+1]
    longest_sub_str = ''

    if (len(sub_s) % 2) == 0:
        left = int(len(sub_s) // 2) - 1
        right = int(len(sub_s) // 2)
    else:
        left = floor(len(sub_s) // 2)
        right = ceil(len(sub_s) // 2)

    while (left >= 0) and (right < len(s)) and sub_s[left] == sub_s[right]:
        longest_sub_str = s[left:right + 1]
        left -= 1
        right += 1

    return longest_sub_str


class Solution:

    def longest_palindrome(self, s: str) -> str:

        len_s = len(s)

        longest_str = ''

        for centre_s in range(len_s):
            sub_s = check_if_palindrome(s, centre_s)

            if len(sub_s) > len(longest_str):
                longest_str = sub_s

        return longest_str


def test_longest_palindrome():
    assert Solution().longest_palindrome("babad") == "bab"
    assert Solution().longest_palindrome("cbbd") == "bb"
    assert Solution().longest_palindrome("b") == "b"
    assert Solution().longest_palindrome("bb") == "bb"


if __name__ == '__main__':
    test_longest_palindrome()
