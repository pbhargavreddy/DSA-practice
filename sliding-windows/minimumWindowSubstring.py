
#leetcode 76
def minimumWindowSubstring_v1(s , t):
    #s = "ADOBECODEBANC"  t = "ABC"   answer -> BANC
    # start from the char which is in t. because minimum
    # 

    N = len(s)
    min_valid = [0,float('inf')]
    
    freq_path = {}

    left =0
    freq_t = {}
    for i in range(len(t)):
        freq_t[t[i]] = freq_t.get(t[i],0) +1

    for right in range(N):
        #Move left to next char that is in t
        while s[left] not in freq_t and left <= right:
            left +=1
        
        freq_path[s[right]]  = freq_path.get(s[right],0) +1 
        # Check if valid and update min_valid
        while(right-left+1 > len(t)):
            if freq_t in freq_path:
                if min_valid[1] > right-left+1:
                    min_valid = [left,right-left+1]
                left +=1
    return s[min_valid[0]:min_valid[1]]
# print(minimumWindowSubstring_v1(s = "ADOBECODEBANC"  ,t = "ABC"))


def minimumWindowSubstring_v2(s , t):
    #s = "ADOBECODEBANC"  t = "ABC"   answer -> BANC
    # start from the char which is in t. because minimum

    min_len = float('inf')
    s_idx = -1

    for i in range(len(s)):
        freq = [0]*256
        count = 0
        for j in range(len(t)):
            freq[ord(t[j])] +=1
        for j in range(len(s)):
            if freq[ord(s[j])] >0:
                count +=1
            freq[ord(s[j])] -=1
            if count == len(t) and j-1+1 < min_len:
                min_len = j-i-1
                s_idx = i
                break

    return s[s_idx:min_len]
            
# print(minimumWindowSubstring_v2(s = "ADOBECODEBANC"  ,t = "ABC"))

def minimumWindowSubstring_v3(s,t):
    min_len = float('inf')
    s_idx = -1
    left = 0
    freq = [0]*256
    for i in range(len(t)):
        freq[ord(t[i])] +=1

    count = 0

    for right in range(len(s)):
        if freq[ord(s[right])] > 0:
            count +=1
        freq[ord(s[right])] -=1

        #if subset is valid
        while count == len(t) :
            if right-left+1 < min_len:
                min_len = right-left+1
                s_idx = left
            
            freq[ord(s[left])] +=1
            if freq[ord(s[left])] >0:
                count -=1 

            left +=1

    return s[s_idx:s_idx+min_len]

print(minimumWindowSubstring_v3(s = "ADOBECODEBANC"  ,t = "ABC"))
