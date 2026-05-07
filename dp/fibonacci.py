def fib_memoization(num,ll):
    if num <= 1:
        return num
    if ll[num] !=-1:
        return ll[num]
    ll[num] = fib_memoization(num-1,ll) + fib_memoization(num-2,ll)

    return ll[num]

def fib_Tabulation(num):
    res=num
    prev2,prev = 0,1
    for _ in range(2,num+1):
        res = (prev2 +prev)
        prev2 = prev
        prev = res
    return res


if __name__ == '__main__':
    
    print(fib_memoization(6,[-1]*21))
    print(fib_Tabulation(6))

    
# s = 'nnvevin envv pm'

# ll = s.split(' ')
# print(ll)