#6
def pissano(m):

    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous+current)%m

        if (previous == 0 and current == 1):
            return i+1

def lastfibbo(n):

    pisano_period = pissano(10)

    n = n%pisano_period
    prev, current = 0, 1

    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range (n-1):
            prev, current = current , (prev + current)%10
        return (current)%10


if __name__ == '__main__':
    input_number = int(input())
    print((lastfibbo((input_number+2))-1 + 10)%10)