#4
def GCD(a,b):
    if b == 0:
        return a
    a_prime = a%b
    return GCD(b, a_prime)

def LCMs(a,b):
    return int((a*b) / GCD(a,b))

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(LCMs(a,b))