def f(k,cnt): # 사용한 종이수, 1 남은 1 개수
    global minpaper, paper, arr
    if cnt==0:
        if minpaper>k:
            minpaper = k
            return
    elif sum(paper)==0:
        return
    elif k>=minpaper:
        return
    else:
        check =1
        i=0
        j=0
        for ix in range(10):
            for jx in range(10):
                if arr[ix][jx]==1:
                    i = ix
                    j = jx
                    check = 0
                    break
            if check == 0:
                break

        # 남은 종이 크기별로 덮어보기
        plist = [5,4,3,2,1]
        for p in plist:
            psum = 0
            for m in range(p):
                for n in range(p):
                    if i+m<10 and j+n<10 and paper[p-1]>0:
                        if arr[i+m][j+n]==1:
                            psum += 1
            if psum==p*p and paper[p-1]>0:
                for m in range(p):
                    for n in range(p):
                        arr[i+m][j+n]=0
                paper[p-1]=paper[p-1]-1
                f(k+1,cnt-p*p)
                for m in range(p):
                    for n in range(p):
                        arr[i+m][j+n]=1
                paper[p-1] = paper[p-1]+1
        return

arr = [list(map(int,input().split())) for i in range(10)]
cnt = 0

for i in arr:
    cnt += i.count(1)

minpaper = 26
paper = [5,5,5,5,5]

f(0,cnt)

if minpaper==26:
    minpaper = -1

print(minpaper)