class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1 for i in range(amount+1)]
        memo[0] = 0 
        
        for i in range(1,len(memo)):
            for c in coins: 
                if i - c >= 0:
                    memo[i] = min(memo[i],1 + memo[i-c])

        return memo[amount] if memo[amount] != amount+1 else -1



        # min_coins = 13
        # grid = [[[] for i in range(len(coins))] for j in range(len(coins))]
        # grid[0][0].append(coins[0])
        # if grid[0][0][0] == amount:
        #     return 1

        # # go through the coins list 
        # for i in range(1,len(coins)):
        #     # go through the combinations 
        #     for j in range(i+1):
        #         # print("j",j,i)
        #         if j == 0:
        #            grid[j][i].append(coins[i]) 
        #         elif j == i:
        #             num = grid[0][i][0] + grid[j-1][i-1][0]
        #             if num == amount:
        #                 min_coins = min(min_coins,j+1)
        #             grid[j][i].append(num) 
        #         else:
        #             for k in range(j-1, i+1-j):
        #                 # print(j-1, k, grid[j-1][k])
        #                 for l in grid[j-1][k]:
        #                     num = grid[0][i][0] + l
        #                     if num == amount:
        #                         min_coins = min(min_coins,j+1)
        #                     grid[j][i].append(num)
        
        # print()
        # if min_coins != 13:
        #     return min_coins
        # return -1
                




        