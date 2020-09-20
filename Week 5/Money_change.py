import numpy as np

def get_change(m):
    Coins = [1,3,4]
    MinNumCoins = np.zeros(m+1, dtype = float)

    for i in range(m):
        MinNumCoins[i+1] = np.inf
        for j in range(len(Coins)):

            
            #print(Coins[j])
            if i+1 >= Coins[j]:

                NumCoins = MinNumCoins[(i+1) - Coins[j]] + 1

                if NumCoins < MinNumCoins[i+1]:

                    MinNumCoins[i+1] = NumCoins
    return int(MinNumCoins[m])

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))