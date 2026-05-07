def perm(i,num):
    if i==len(num):
        print(num)
    for j in range(i,len(num)):
        num[i],num[j] = num[j] ,num[i]
        perm(i+1,num)
        num[i],num[j] = num[j] ,num[i]
perm(0,[1,2])