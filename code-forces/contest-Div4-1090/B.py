def solve():
    n = int(input())

    for i in range(n):
        l = list(map(int , input().split()))
        print(2*max(l)-sum(l))

if __name__ == '__main__':
    solve()