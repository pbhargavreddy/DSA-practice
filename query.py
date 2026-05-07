def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    res = 0
    q = int(input())
    for i in range(q):
        query , l , r = map(int,input().split())
        # code here
        if query == 1:
            for i in range(l,r+1):
                arr[i] = arr[l]*(i-l+1)
        else:
            res += sum(arr[l:r+1])
    return res

if __name__ == "__main__":
    solution = solve()
    print(solution)