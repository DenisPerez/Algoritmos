#1
def fibbo (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        initial = [0,1]

        for i in range(n):
            prev_sum = initial[0] + initial[1]
            initial[0] = initial[1]
            initial[1] = prev_sum
        return initial[0]

if __name__ == '__main__':
    input_n = int(input())

    print(fibbo(input_n))