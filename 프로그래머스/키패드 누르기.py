def solution(numbers, hand):
    answer = ''
    left, right='*','#'          # 현재 손의 위치
    lidx,ridx=0,2                # 현재 손이 arr 리스트에서 어느 열에 있는지, index() 함수에 사용
    arr=[['1','4','7','*'],['2','5','8','0'],['3','6','9','#']]
    
    for num in numbers:
        if str(num) in arr[0]:
            answer+='L'
            left=num
            lidx=0
        elif str(num) in arr[2]:
            answer+='R'
            right=num
            ridx=2
        else:
            L_dst=abs(arr[1].index(str(num))-arr[lidx].index(str(left)))
            if lidx!=1:
                L_dst+=1
            R_dst=abs(arr[1].index(str(num))-arr[ridx].index(str(right)))
            if ridx!=1:
                R_dst+=1
            if L_dst<R_dst:
                answer+='L'
                left=num
                lidx=1
            elif L_dst>R_dst:
                answer+='R'
                right=num
                ridx=1
            else:
                if hand=='left':
                    answer+='L'
                    left=num
                    lidx=1
                else:
                    answer+='R'
                    right=num
                    ridx=1
            
    return answer
