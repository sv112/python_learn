
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_chars = {}
        local_longest_s = ''
        longest_s = ''

        for char_ in s:
            if char_ not in hash_chars:
                local_longest_s += char_
                hash_chars[char_] = None
            else:
                if len(local_longest_s) > len(longest_s):
                    longest_s = local_longest_s
                local_longest_s = char_
                hash_chars = {char_: None}

        return longest_s


def test_longest_substring():
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(s) == 'abc'

    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring(s) == 'b'

    s = "pwwkew"
    assert Solution().lengthOfLongestSubstring(s) == 'wke'

