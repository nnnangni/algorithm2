import copy
def attack(position,field):
    global N, M, D,cnt
    zero=0

    # 필드에서 남아있는 0값 찾기
    for fi in field:
        for f in fi:
            if f==0:
                zero += 1
    # 남아있는 0들이 배열의 크기랑 같으면 리턴
    if zero==N*M:
        return cnt
    # 궁수 위치에서 예) position=[0,1,2]
    shoot = []
    for p in position:
        go = True
        wait = []
        for i in range(N-1,-1,-1):
            # 아래부터 위로 올라가면서 찾으면 가까운거 찾을수 있을거같아서? 이렇게함
            for j in range(M-1,-1,-1):
                dis = abs(i-N) + abs(j-p)
                if dis<=D:
                    if field[i][j]==1:# 공격거리안에 들면
                        wait.append([i,j,dis]) # 0으로 바꿔주고
        if len(wait)>=1:
            d = wait[0][2]
            for w in wait:
                if w[2]<=d:
                    d=w[2]

            for i in wait:
                if i[2]==d:
                    shoot.append([i[0],i[1]])
                    break

    for s in shoot:
        if field[s[0]][s[1]]==1:
            field[s[0]][s[1]]=0
            cnt+=1


    # 한칸씩 전진~~
    newfield = [[0]*M for i in range(N)]
    for c in range(N):
        if c+1<N:
            temp = field[c][:]
            newfield[c+1]=field[c]
    attack(position,newfield)

# 궁수위치
def f(n,m,c,before):
    global position,cnt,kill,origin
    if n==c:
        cnt = 0 # 죽인 수 찾기
        field=copy.deepcopy(origin) # 다시 배열 초기화
        # 죽이기 시작~~
        attack(position,field)
        # 죽인 수 추가하기
        kill.append(cnt)
        return position
    else:
        for i in range(before,m):
            if used[i]==0:
                used[i]=1
                position[n]=plist[i]
                f(n+1,m,c,i)
                used[i]=0

# 여기서 시작!!
N, M, D = map(int,input().split())
origin = [list(map(int,input().split())) for i in range(N)]
# field = 깊은 복사로 바꿔줄 필드
field = copy.deepcopy(origin)
# 조합구하기
plist = [i for i in range(M)]
C = 3
used = [0]*M
position = [0]*C
# 궁수위치마다 kill값 저장해서 최대값 찾기위해 만든 리스트
kill = []
# 조합으로 궁수위치 찾기
f(0,M,C,0)

mk = max(kill)
print(mk)
