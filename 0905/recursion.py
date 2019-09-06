# 멱집합 {1,2,3} - 모든 부분집합 구하기
select=[False,False,False]
def powerset(select,depth):
    print(select,depth)
    print()
    if depth==len(select):
        # 여기서 원하는 부분집합을 구하게 됨
        print("내 부분집합",select,depth)
        print()
        return
    select[depth] = True # 해당 숫자를 집합에 사용하겠다.
    powerset(select,depth+1)
    select[depth]= False # 해당 숫자를 집합에 사용하지 않겠다.
    powerset(select,depth+1)

powerset(select,0)