import heapq as q
from typing import List

def solve(nums : List[int]):
    num = []
    q.heapify(nums)
    for i in range(len(nums)):
        num.append(q.heappop(nums))
        q.heapify(nums)
    print(num)
    

if __name__ == '__main__':
    solve([2,4,1,6,8,0,5])
