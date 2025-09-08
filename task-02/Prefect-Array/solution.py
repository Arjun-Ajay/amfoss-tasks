def isEven(i:int):
    if i&1==0:
        return True
    else:
        return False

def fromMinSide(input_arr:list):
    arr=input_arr.copy()
    op=0
    if isEven(arr[0])==True:
        while isEven(arr[-1])==False:
            op+=1
            arr.pop()
        return op
    else:
        while isEven(arr[-1])==True:
            op+=1
            arr.pop()
        return op

def fromMaxSide(input_arr:list):
    arr=input_arr.copy()
    op=0
    arr.sort(reverse=True)
    if isEven(arr[0])==True:
        while isEven(arr[-1])==False:
            op+=1
            arr.pop()
        return op
    else:
        while isEven(arr[-1])==True:
            op+=1
            arr.pop()
        return op

test_case=int(input())
while test_case:
    size=int(input())
    input_vals=list(map(int,input().split())) #2 7 4 6 9 11 5
    input_vals.sort()
    LHS=fromMinSide(input_vals)
    RHS=fromMaxSide(input_vals)
    if LHS<=RHS:
        print(LHS)
    else:
        print(RHS)
    test_case-=1