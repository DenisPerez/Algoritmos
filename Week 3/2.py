def maximun_value(objects, W):
    value = 0
    
    for i in range(n):
        if(W == 0):
            return(value)
        a = min(objects[i][1], W)
        value = value + a * (objects[i][0]/objects[i][1])
        objects[i][1] = objects[i][1] - a
        W = W - a
    return value

if __name__ == '__main__':
    n, W = map(int, input().split())
    objects = []
    for _ in range(n):
        v,w = map(int, input().split())
        empty_list = []
        empty_list.append(v)
        empty_list.append(w)
        objects.append(empty_list)
    objects = sorted(objects, key=lambda x: x[0]/x[1], reverse=True)
    print(maximun_value(objects,W))