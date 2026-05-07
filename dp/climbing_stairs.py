dp = [0]*(5+1)

def climb(n):
    if dp[n] !=0 :
        return dp[n]
    if n==0:
        return 1
    if n<0:
        return 0
    dp[n] = climb(n-1) + climb(n-2)
    return dp[n]
if __name__ == '__main__':
    n=5
    print(climb(n))