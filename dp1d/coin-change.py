class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # T: O(amount * len(coins) M: O(amount)
        #if start with all zeros, then need manual tracking of min below
        dp = [0] * (amount + 1) #start with this as base value


        #imagine dp is from 0 left to amount left
        for i in range(1, amount + 1):
            minCoins = float("inf")
            #have to try every coin
            for c in coins:
                #if in bounds to try with coin c and there is a path
                if i >= c and dp[i - c] != -1:
                    #try to find minimum to get to this amount
                    minCoins = min(minCoins, 1 + dp[i - c])

            if minCoins == float("inf"):
                dp[i] = -1
            else:
                dp[i] = minCoins

        return dp[amount]








        


        
