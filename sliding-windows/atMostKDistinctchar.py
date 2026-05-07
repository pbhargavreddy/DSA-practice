def longestAtMostKDistinctChar(s,k):
    #eceba  , k = 2 answer: 3 -> ece

    #Logic
    # Maintain a window dinamically. shrink whenever the len(freq) surpasess. update max_len every time window is expanded
    max_len = 0
    freq = {}
    left = 0
    N = len(s)

    for right in range(N):
        #expand
        freq[s[right]] = freq.get(s[right],0) +1
        #shrink
        while(len(freq) > k):
            freq[s[left]] -=1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left +=1
        # Update after shrinking
        max_len = max(max_len , right -left +1)
    return max_len
print(longestAtMostKDistinctChar('ececba',2))