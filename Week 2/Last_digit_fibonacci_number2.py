#2
def fibbolastnumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        initial_last_digits = [0,1]
        for i in range(n):
            prev_last_digit = initial_last_digits[0] + initial_last_digits[1]
            initial_last_digits[0] = initial_last_digits[1]
            initial_last_digits[1] = prev_last_digit%10

        return initial_last_digits[0]

if __name__ == '__main__':
    input = int(input())
    print(fibbolastnumber(input))