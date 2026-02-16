import itertools

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        len_s = len(s)

        temp_row = list(range(len_s))

        mask_l = [*list(range(numRows)), *list(range(numRows -2,  0, -1))]
        mask = itertools.cycle(mask_l)
        row_idx = 0
        final_rows = [ [] for _ in range(numRows) ]

        while row_idx < len(temp_row):
            row = next(mask)
            final_rows[row].append(temp_row[row_idx])
            row_idx += 1

        final_str = [s[idx] for idx in itertools.chain(*final_rows)]

        return ''.join(final_str)


def test_zig_zag():
    assert Solution().convert("AEPLIPM", 3) == "AIELPPM"
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
    assert Solution().convert("A", 1) == "A"
    assert Solution().convert("A", 2) == "A"
    assert Solution().convert("AB", 3) == "AB"
    assert Solution().convert("ABC", 2) == "ACB"
    assert Solution().convert("ABCDEF", 2) == "ACEBDF"
    assert Solution().convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"


if __name__ == '__main__':
    test_zig_zag()
