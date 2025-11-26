#Sorted Coins Problem

def return_coins(coins, target_amount):
    if target_amount < 0:
        print("Error: No negative money!")

    sorted_coins = sorted (coins, reverse = True)

    change = []

    for coins in sorted_coins:
        while target_amount >= coins:    
            change.append(coins)
            target_amount -=coins

    return change

#Testing
coins = [1, 5, 10, 25, 100]
amount = 10
print(f"Target: {amount} - {return_coins(coins,amount)}")

amount = 35
print(f"Target: {amount} - {return_coins(coins,amount)}")

amount = -10
print(return_coins(coins,amount))

amount = 0.5
print(f"Target: {amount} - {return_coins(coins,amount)}")

print("Different coins")
coins2 = [1, 2, 3, 5, 10, 20, 50 , 100]
amount = 47
print(f"Target: {amount} - {return_coins(coins,amount)}")
