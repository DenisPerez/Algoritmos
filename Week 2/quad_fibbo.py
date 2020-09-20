#8
def pissano(m):

    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous+current)%m

        if (previous == 0 and current == 1):
            return i+1

def lastfibbo(n,m):

    pisano_period = pissano(m)

    n = n%pisano_period

    previous, current = 0,1

    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range (n-1):
            previous, current = current, previous + current

    return (current % m)



if __name__ == '__main__':
    n = int(input())
    partial_sum = ((lastfibbo(n,10)+ 10) * lastfibbo(n+1,10))%10
    
    print(partial_sum)