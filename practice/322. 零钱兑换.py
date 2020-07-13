# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。

class Solution(object):
    def __init__(self):
        self.note = dict()

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = float('INF')
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        for coin in coins:
            if self.note.get(amount):
                return self.note.get(amount)
            sub_problem = self.coinChange(coins, amount - coin)
            if sub_problem == -1:
                continue
            res = min(res, sub_problem + 1)
        res = res if res != float('INF') else -1
        self.note[amount] = res
        return res


if __name__ == '__main__':
    cc = Solution().coinChange([1, 2, 5], 12)
    print(cc)
