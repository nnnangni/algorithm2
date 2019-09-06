def powerset(n,k):
    global check
    if n==k:
        print(*check)
        return
    else:
        check[n]=0
        powerset(n+1,k)
        check[n]=1
        powerset(n+1,k)

arr = [1,2,3]
k = len(arr)
check = [0]*k
powerset(0,k)

# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1