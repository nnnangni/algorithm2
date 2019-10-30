import copy
def bfs(a,b):
    global maparr, land, landp,queuex,queuey
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    i = queuex.pop(0)
    j = queuey.pop(0)
    for f in range(4):
        nx = i + dx[f]
        ny = j + dy[f]
        if 0<=nx<N and 0<=ny<N:
            if maparr[nx][ny]==1 and visited[nx][ny]==0:
                landp.append([nx,ny])
                visited[nx][ny]=1
                queuex.append(nx)
                queuey.append(ny)
                bfs(nx,ny)
    if len(queuex) == 0 and len(queuey) == 0:
        return


def bridge(connect):
    global land, find
    b1 = land[connect[0]]
    b2 = land[connect[1]]

    minx = 10
    for b in b1:
        for c in b2:
            if b[0]==c[0]:
                if minx>abs(b[1]-c[1])-1:
                    minx = abs(b[1]-c[1])-1
            if b[1]==c[1]:
                if minx>abs(b[0]-c[0])-1:
                    minx = abs(b[0]-c[0])-1

    if minx!=10:
        cn.append(connect[:])
        mx.append(minx)


def f(n,island,c,before):
    global combi, connect, used
    if n==c:
        bridge(connect)
        return
    else:
        for i in range(before,island):
            if used[i]==0:
                used[i]=0
                connect[n]=combi[i]
                f(n+1,island,2,i+1)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maparr = [list(map(int,input().split())) for i in range(N)]
    visited = [[0]*N for i in range(N)]
    landlist = []
    land = []
    for i in range(N):
        for j in range(N):
            if maparr[i][j]==1 and visited[i][j]==0:
                queuex=[]
                queuey=[]
                queuex.append(i)
                queuey.append(j)
                landp = [[i,j]]
                visited[i][j]=1
                bfs(i,j)
                land.append(landp)
    island = len(land)
    c = 2
    combi = [i for i in range(0,island)]
    connect = [0]*c
    used = [0]*island
    cn = []
    mx = []
    f(0,island,c,0)
    num = len(cn)
    new = [[0]*num for i in range(num)]
    for idx,val in enumerate(cn):
        new[val[0]][val[1]]=mx[idx]

    dis = 0
    for n in new:
        mindis = 10
        for i in n:
            if i!=0:
                if i<mindis:
                    mindis = i
        if mindis!=10:
            dis+=mindis
    if dis==0:
        dis=-1
    print("#{} {}".format(tc,dis))