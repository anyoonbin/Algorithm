for test_case in range(1, 11):
    secure_num = int(input())
    secure_list = list(map(str, input().split()))
    cmd_num = int(input())
    cmd_list = list(map(str, input().split()))
    i, cnt=0,0
    
    while cnt<cmd_num:
        if cmd_list[i]=='I':
            secure_list=secure_list[0:int(cmd_list[i+1])]+cmd_list[i+3:i+3+int(cmd_list[i+2])]+secure_list[int(cmd_list[i+1]):secure_num+1]
            i+=(3+int(cmd_list[i+2]))
       
        elif cmd_list[i]=='D':
            secure_list=secure_list[0:int(cmd_list[i+1])]+secure_list[int(cmd_list[i+1])+int(cmd_list[i+2]):secure_num+1]
            i+=3
            
        elif cmd_list[i]=='A':
            secure_list.extend(cmd_list[i+2:i+2+int(cmd_list[i+1])])
            i+=(2+int(cmd_list[i+1]))
            
        cnt+=1
        secure_num=len(secure_list)
    print("#%d" %test_case, ' '.join(secure_list[0:10]))
