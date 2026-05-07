def isSubsequence(s: str, t: str) -> bool:
        i =0
        for char in s:
            if i ==len(s):
                 break
            if char == t[i]:
                i+=1
        print(i)
        return i==len(s)
print(isSubsequence("axc","ahbgdc"))