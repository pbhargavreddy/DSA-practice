def power_set(arr):
    res=[]
    subset =[]
    def backtrack(i=0):
        if i==len(arr):
            res.append(subset.copy())
            return
        subset.append(arr[i])
        backtrack(i+1)
        subset.pop()
        backtrack(i+1)
    backtrack()
    return res


print(power_set([1,2,3]))


def power__set(arr,res = [],subset=[],i=0):
    if i==len(arr):
        return res.append(subset)
    power__set(arr,res,subset+[arr[i]],i+1)
    power__set(arr,res,subset,i+1)
    return res
a = power__set([1,2,3])
print(a)