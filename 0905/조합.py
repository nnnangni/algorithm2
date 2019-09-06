def combination(n,k,c,before):
    global result
    if n==c:
        print(*result)
        return
    else:
        for i in range(before,k):
            if used[i]==0:
                used[i]=1
                result[n]=arr[i]
                combination(n+1,k,c,i)
                used[i]=0

arr = [1,2,3]
k = len(arr)
c = 2
used = [0]*k
result = [0]*c
combination(0,k,c,0)

# 1 2
# 1 3
# 2 3