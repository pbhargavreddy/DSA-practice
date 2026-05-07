# j=0 
s = "the sky is blue"
# words=[]
# while(s[j]==' '):
#     j+=1

# i=j+1
# while(i<len(s)):
#     if(s[i] == ' '):
#         words.append(s[j:i])
#         while(i < len(s) and s[i]==' '):
#             i+=1
#         j = i
#     else:
#         i+=1

# print(words)

def reverseWords(s: str) -> str:
        res  = ''
        j=0
        words=[]
        while(s[j]==' '):
            j+=1
        i=j+1
        while(i<len(s)):
            if(s[i] == ' '):
                words.append(s[j:i])
                while(i<len(s) and s[i]==' '):
                    i+=1
                j=i
            else:
                i+=1
        if(j<len(s)):
            words.append(s[j:i])
        print(words)
        for i in range(len(words)-1,-1,-1):
            if i ==0:
                res += words[i]
            else:
                res += words[i]+' '
        

        return res

print(reverseWords(s))