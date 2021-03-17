def solution(m, musicinfos):
    m_list=[]
    answer=''
    answer_t=0
    temp=''
    for i in m:
        if i=='#':
            temp+=i
        else:
            m_list.append(temp)
            temp=i
    m_list.append(temp)
    m_list=m_list[1:]

    for i in musicinfos:
        music=''
        info=i.split(',')
        li=[]
        temp=''
        for i in info[3]:
            if i=='#':
                temp+=i
            else:
                li.append(temp)
                temp=i
        li.append(temp)
        li=li[1:]
        t=(int(info[1][:2])-int(info[0][:2]))*60+(int(info[1][3:])-int(info[0][3:]))
        s=li*(t//len(li))+li[:t%len(li)]
        for i in range(t):
            if s[i]==m_list[0] and len(s)-i>=len(m_list):
                if m_list==s[i:i+len(m_list)] and answer_t<t:
                    answer=info[2]
                    answer_t=t

    return answer if answer else '(None)'
