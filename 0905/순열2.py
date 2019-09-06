arr = [1,2,3]
k = len(arr)
c = 2
used =[0]*k
p=[0]*c

def f(n,k,c):
    if n == c:
        print(*p)
    else:
        for i in range(k):
            if used[i]==0:
                used[i]=1
                p[n] = arr[i]
                f(n+1,k,c)
                used[i]=0
f(0,k,c)

# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2