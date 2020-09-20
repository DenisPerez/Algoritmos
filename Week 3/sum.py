def suma_mitad(li,ls):
    interval = (ls-li)+1
    interval = interval//2
    return((li+interval))

if __name__ == '__main__':
    while(True):
        li, ls = map(int,input().split())
        print(suma_mitad(li,ls), li, ls)

