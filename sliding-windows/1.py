s ="aaababaaabbbcccbca"
k = 3
left =0
freq ={}
for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1

            if min(freq.values()) <k:
                freq[s[left]] = freq.get(s[left],0) - 1
                if freq[s[left]] ==0:
                        del freq[s[left]]
                left +=1
            if min(freq.values()) >= 2:
                    print(freq)