def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


if __name__ == '__main__':
    n = int(input())
    data = list(map(int,input().split()))
    print(int(get_majority_element(data,0,n) != -1))