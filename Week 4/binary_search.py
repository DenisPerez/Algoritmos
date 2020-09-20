def binary_search_iterative(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1



if __name__ == '__main__':
    _, *data = map(int,input().split())
    m, *find = map(int, input().split())
    for x in find:
        print(binary_search_iterative(data, x), end = ' ')