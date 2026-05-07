def solve():
    n = int(input())
    known = []
    count = 0
    for i in range(n):
        path = list(map(int , input().split()))
        if sum(path) >=2:
            count +=1
    print(count)

if __name__=="__main__" :
    solve() 