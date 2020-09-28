"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:  # 右边顺序
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:  # 左边顺序
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    index = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
