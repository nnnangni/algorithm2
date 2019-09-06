arr = [1,2,3]
k = len(arr)
used =[0]*k
p=[0]*k

def f(n,k):
    if n == k:
        print(*p)
    else:
        for i in range(k):
            if used[i]==0:
                used[i]=1
                p[n] = arr[i]
                f(n+1,k)
                used[i]=0
f(0,k)

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1