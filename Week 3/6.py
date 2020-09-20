def maximun_number_prizes(n):
    prizes = []
    quitar = 1
    prizes.append(quitar)
    n = n - quitar
    quitar += 1
    while(n!=0):
        if((n - quitar) < 0):

            prizes[len(prizes)-1] += n
            n = 0
        else:
            
            n = n - quitar
            prizes.append(quitar)
            quitar += 1

    return prizes

#(n - quitar) <= prizes[len(prizes)-1] and (n - quitar) > 0 )


if __name__ == '__main__':
    n = int(input())
    prizes = maximun_number_prizes(n)
    print(len(prizes))
    for p in prizes:
        print(p, end=' ')
