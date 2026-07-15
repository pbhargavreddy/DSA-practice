def perm(i,path):
    if i==len(path):
        print(path)
    for j in range(i,len(path)):
        path[i],path[j] = path[j] ,path[i]
        perm(i+1,path)
        path[i],path[j] = path[j] ,path[i]
perm(0,[1,2,3]) 