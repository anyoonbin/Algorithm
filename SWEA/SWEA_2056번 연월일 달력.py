T = int(input())
mon=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    bol=False
    day=str(input())
    if int(day[0:4])>0:
        if 0<int(day[4:6])<13:
            if 0< int(day[6:8])<=mon[int(day[4:6])-1]:
                bol=True
    print("#%d" %test_case, end=" ")
    print(day[0:4], day[4:6], day[6:8], sep="/") if bol==True else print(-1)
