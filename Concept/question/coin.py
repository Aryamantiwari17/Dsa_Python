#Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. 
#Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or 
#report that it’s not possible to select coins in such a way that they sum up to S For a better understanding 
#let’s take this example: Given N = 3 ,no of coins, sum S is set to be 11. 
# coins with values 1, 3, and 5. So, min no of coins required for the sum 11 would be 3. ie Two 5 sum coin and one 1 coin.
def min_coins_needed(coins, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    
    for coin in coins:
        for j in range(coin, target_sum + 1):
            dp[j] = min(dp[j], 1 + dp[j - coin])
    
    if dp[target_sum] == float('inf'):
        return -1
    else:
        return dp[target_sum]

# Input: Number of coins
N = int(input("Enter the number of coins: "))

# Input: Coin values
coins = []
for _ in range(N):
    coin_value = int(input("Enter coin value: "))
    coins.append(coin_value)

# Input: Target sum
target_sum = int(input("Enter the target sum: "))

result = min_coins_needed(coins, target_sum)

if result == -1:
    print("It's not possible to select coins in such a way that they sum up to", target_sum)
else:
    print("Minimum number of coins needed for the sum", target_sum, "is", result)
4