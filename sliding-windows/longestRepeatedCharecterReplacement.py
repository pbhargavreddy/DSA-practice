def longestReaptedsubstring1(s , k)->int:
    # Brute Force
    max_len = 0
    N = len(s)
    substrs = []
    for i in range(N):
        for j in range(i,N):
            substrs.append(s[i:j+1])
    for substr in substrs:
        freq = [0]*26
        for i in range(len(substr)):
            freq[ord(substr[i]) - ord('a')] +=1
        max_freq = max(freq)
        if len(substr) - max_freq <= k:
            max_len = max(max_len,len(substr))
    
    return max_len

print(longestReaptedsubstring1('aababba',2))

def longestReaptedsubstring2(s,k):
# Optimized 
    max_len = 0
    max_freq = 0
    N = len(s)

    left = 0
    freq = [0]*26

    for right in range(N):
        # always expand
        idx = ord(s[right]) - ord('a')
        freq[idx] +=1
        #insead finding max freq every time. Use previous computation. Max every time would take o(26). and multiplied by N
        # max_freq = max(freq)
        max_freq = max(max_freq,freq[idx])
        substr_len = right-left + 1
        # shrink
        while substr_len - max_freq >k:
            freq[ord(s[left]) - ord('a')] -=1
            left +=1
        # update max
        max_len = max(max_len,substr_len)
    return max_len

print(longestReaptedsubstring2('aababba',3))