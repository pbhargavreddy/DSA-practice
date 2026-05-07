from typing import List
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(idx,s,arr):
            if s== target:
                res.append(arr.copy())
                return
            if s>target:
                return
            for i in range(idx,len(candidates)):
                arr.append(candidates[i])
                s += candidates[i]
                backtrack(idx+1 , s,arr)
                s-=arr.pop()
        backtrack(0,0,[])
        return res
print(combinationSum([2,3,6,7],7))