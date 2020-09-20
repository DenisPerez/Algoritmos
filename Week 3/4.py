# python3
def max_dot_product(a,b):
    res = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        res += a[i] * b[i]
    
    return res

if __name__ == '__main__':
    n = int(input())
    [*a] = map(int,input().split())
    [*b] = map(int,input().split())
    print(max_dot_product(a,b))