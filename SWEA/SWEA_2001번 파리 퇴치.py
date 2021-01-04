T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    N_list=[]
    num=0
    for i in range(n):
        N_list.append(list(map(int, input().split())))
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp=0
            for k in range(m):
                temp+=sum(N_list[i+k][j:m+j])
                if num<temp:
                    num=temp
    print("#%d" %test_case, num)
