def solve():
    N = int(input())
    C = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))

    initial_oil = 0
    curr_oil = 0
    for i in range(N):
        if arr[i] ==-1:
            if curr_oil <= 0:
                initial_oil +=1
                curr_oil = 0
            else:
                curr_oil -=1
        else:
            if curr_oil >= C:
                curr_oil = C
            else:
                curr_oil +=1
    return initial_oil 


if __name__ == '__main__':
    print(solve())