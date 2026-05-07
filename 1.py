nums = [1,1,2,3,2,4,5]

for i in range(1,len(nums)):
    nums[i]  += nums[i-1]

print(nums)

print(nums[6]-nums[3])  # sum of suubarray from idx 3+1 to 6