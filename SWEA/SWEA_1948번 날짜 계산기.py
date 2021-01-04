T = int(input())
mon=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    print("#%d" %test_case, sum(mon[li[0]:li[2]-1])+(mon[li[0]-1]-li[1])+li[3]+1) if li[0]!=li[2] else print("#%d" %test_case, li[3]-li[1]+1) 
