def solve(nums):
    def recursion(idx):
        if idx == 0:
            return nums[idx]
        if idx <0:
            return 0
        left = nums[idx] + recursion(idx-2)
        right = recursion(idx-1)

        return max(left,right)
    
    def dynamic_prog(idx,dp):
        # memoization
        if idx == 0:
            return nums[idx]
        if idx <0:
            return 0
        if dp[idx] !=-1:
            return dp[idx]
        left = nums[idx] + dynamic_prog(idx-2,dp)
        right = dynamic_prog(idx-1,dp)
        dp[idx] =max(left,right)

        return dp[idx]
    

    def dynamic_prog_tabulation():
        dp = [-1]*(len(nums))
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            take = nums[i]
            if i>=2:
                take += dp[i-2]
            not_take = dp[i-1]
            dp[i] = max(take,not_take)
        return dp[-1]
    
    print(recursion(len(nums)-1))
    print(dynamic_prog(len(nums)-1,[-1]*(len(nums))))
    print(dynamic_prog_tabulation())

solve([2,7,9,3,1])