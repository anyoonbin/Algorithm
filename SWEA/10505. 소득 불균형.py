T = int(input())

for test_case in range(1, T + 1):
    num=int(input())
    li = list(map(int, input().split()))
    avg = sum(li)//num
    print("#%d" %test_case,len(list(filter(lambda x: x <= avg, sorted(li)))))
