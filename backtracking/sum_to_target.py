#print all results
def sumEqualToTargett(arr,target):
    res = []

    def backtrack(idx,a,s):
        if s==target:
            res.append(a.copy())
            return
        if idx == len(arr) or s>target:
            return
        a.append(arr[idx])
        s += arr[idx]
        backtrack(idx+1,a,s)
        s -= a.pop()
        backtrack(idx+1,a,s)
    backtrack(0,[],0)
    return res
print(sumEqualToTargett([1,2,1],2))

#print any one result
def sumEqualToTarget(arr,target):
    res = []

    def backtrack(idx,a,s):
        if s==target:
            res.append(a.copy())
            return True
        if idx == len(arr) or s>target:
            return False
        a.append(arr[idx])
        s += arr[idx]
        if(backtrack(idx+1,a,s)): return True
        s -= a.pop()
        if(backtrack(idx+1,a,s)): return True
        return False
    backtrack(0,[],0)
    return res
print(sumEqualToTarget([1,2,1],2))