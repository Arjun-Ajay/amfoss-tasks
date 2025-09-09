test_case=int(input())
while test_case:
    n=int(input())
    x,y=map(int,input().split())
    val=min(x,y)
    if n%val==0:
        print(int(n/val))
    else:
        print(int(n//val+1))
    test_case-=1