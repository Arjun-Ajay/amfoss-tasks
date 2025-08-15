def check_xy(a,x,y):
    Min=min(x,y)
    Max=max(x,y)
    if a>Min and a<Max:
        return 0
    else:
        return 1

tries=int(input())
while tries:
    a,x,y=map(int,input().split())
    flag=0
    flag=check_xy(a,x,y)
    if flag==0:
        print("NO")
    else:
        print("YES")
    tries-=1