def optimal_points(segments):
    points = []
    segments = sorted(segments, key = lambda x: x[1])
    current = segments[0][1]
    segments.pop(0)
    points.append(current)
    for i in range(len(segments)):
        if((current < segments[i][0]) or (current > segments[i][1])):
            current = segments[i][1]
            points.append(current)
    return points
        



if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        input_segement = []
        a, b = map(int, input().split())
        input_segement.append(a)
        input_segement.append(b)
        segments.append(input_segement) 
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
