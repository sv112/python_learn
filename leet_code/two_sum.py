from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:

    idx_hash = {}
    for idx, val in enumerate(nums):
        if (target - val) in idx_hash:
            return [idx_hash[target - val], idx]
        idx_hash[val] = idx

    return []


def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]


if __name__ == '__main__':
    test_two_sum()
