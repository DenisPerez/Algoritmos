def isgreaterorequal(digit, maxdigit):
    return int(str(digit) + str(maxdigit)) >= int((str(maxdigit) + str(digit)))

def largest_number(lst):
    answer = []

    while lst!= []:
        max_digit = 0
        for digit in lst:
            if isgreaterorequal(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)
    return answer

if __name__ == '__main__':
    n = int(input())
    [*data] = map(int, input().split())
    print(''.join([str(i) for i in largest_number(data)]))