"""
TODO
Ref: https://leetcode.com/problems/coin-change/

Interview: Arzoo
Date : 10-Oct-2022
Difficulty : Medium

Topic: Dynamic Programming

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        total_coins = 0
        coins.sort()
        coin_ptr = len(coins) - 1
        left = amount
        
            
        def change(coin_ptr, left, total_coins):
            print(coin_ptr, left, total_coins)

            if left == 0:
                return total_coins, left
            elif coin_ptr <= -1:
                return total_coins, left
            else:
                if coins[coin_ptr] <= left:

                    ## Case 1 : Take it

                    count1, left1 =  change(coin_ptr,left - coins[coin_ptr],total_coins)
                    count2, left2 = change(coin_ptr-1,left,total_coins)
                    
                    if count1 < count2:
                        total_coins += count1
                        left = left1
                    else:
                        total_coins += count2
                        left = left2
                else:
                    ## Skip
                    tc, left = change(coin_ptr-1,left,total_coins)
                    total_coins += tc
                
                return total_coins, left
                    

        total_coins, left = change(coin_ptr,left,total_coins)
        if left == 0 :
            return total_coins
        else:
            return -1