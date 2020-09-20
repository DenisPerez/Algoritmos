def car_fueling(distance, tank, stations ):
    last_refill = 0
    tank_ = tank
    actual = 0
    iterator = 0
    num_refill = 0
    while(actual != distance):
        if(can_travel(stations[iterator], stations[iterator+1], tank)):
            if(tank_ - (stations[iterator+1] - stations[iterator]) < 0):
                last_refill = stations[iterator]
                num_refill = num_refill +1
                tank_ = tank
            else:
                actual = stations[iterator+1]
                tank_ = tank_ - (stations[iterator+1] - stations[iterator])
                iterator = iterator + 1
        else:
            return -1
    return num_refill

def can_travel(act, next, tank):
    if ((next-act) <= tank):
        return True
    else:
        return False

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stations_input = input()
    stations = []
    stations.append(0)
    for i in range(n):
        stations.append(int(stations_input.split()[i]))
    stations.append(d)
    print(car_fueling(d,m,stations))