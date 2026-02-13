from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n_1 = len(nums1)
        n_2 = len(nums2)

        prev_val = next_val = None
        idx_1 = idx_2 = 0

        for i in range(int((n_1 + n_2) / 2)):
            if nums1[i] > nums2[i]:
                prev_val = nums1[i]
                idx_1 += 1
            else:
                prev_val = nums2[i]
                idx_2 += 1

        if (idx_1 >= n_1):
            next_val = nums2[idx_2]

            nums1[idx_1]  or (nums1[idx_1] > nums2[idx_2]) else nums2[idx_2]

        if (n_1 + n_2) % 2 == 0:
            median = (prev_val + next_val) / 2
        else:
            median = next_val

        return median


def test_median_vals():
    nums1 = [1, 3]
    nums2 = [2]

    Solution().findMedianSortedArrays(nums1, nums2)


if __name__ == '__main__':
    test_median_vals()