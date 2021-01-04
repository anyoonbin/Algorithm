T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle=[]
    answer=0
    for i in range(n):
        puzzle.append(list(map(int, input().split())))
    for i in range(n):
        rcnt,dcnt=0,0
        for j in range(n):
            if puzzle[i][j]==1:
                rcnt+=1
            else:
                rcnt=0
            if puzzle[j][i]==1:
                dcnt+=1
            else:
                dcnt=0
            if rcnt==k and (puzzle[i][j+1]!=1 if j<n-1 else True):
                answer+=1
                rcnt=0
            if dcnt==k and (puzzle[j+1][i]!=1 if j<n-1 else True):
                answer+=1
                dcnt=0
    print("#%d" %test_case, answer)
