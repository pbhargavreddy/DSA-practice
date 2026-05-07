import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    for i in range(n):
        s = input()[:-1]
        if len(s) > 10:
            res = s[0] + str(len(s)-2) + s[-1]
            print(res)
        else:
            print(s)

if __name__ == '__main__':
    solve() 