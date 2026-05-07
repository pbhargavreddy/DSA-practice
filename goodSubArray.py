def solve():
    n = int(input())
    k = int(input())
    arr = []
    for i in range(n):
          arr.append(int(input()))
    max_sum = 0

    l = 0 
    freq = {}
    curr_sum = 0

    for r in range(n):
        freq[arr[r]] = freq.get(arr[r],0)+1
        curr_sum += arr[r]
        #shrink
        while(len(freq)>k):
            freq[arr[l]] -=1
            curr_sum -= arr[l]
            if freq[arr[l]] == 0:
                del freq[arr[l]]
            l +=1
        #compare and update sum
        max_sum = max(max_sum,curr_sum)
    
    return max_sum

if __name__ == '__main__':
    solution = solve()
    print(solution)