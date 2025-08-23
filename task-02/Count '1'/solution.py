def flipper(givenString:str,position:int):
    if int(givenString[position])==1:
        newString=givenString[:position]+"0"+givenString[position+1:]
        return newString
    else:
        newString=givenString[:position]+"1"+givenString[position+1:]
        return newString

def count1s(givenString):
    count=loop=condition=0
    #print("givenString:",givenString)
    for i in givenString:
        #print("loop:",loop)
        #print("i:",i)
        if i=="1":
            count+=1
            #print("condition:",condition)
            #print("count:",count)
            condition+=1
        loop+=1
    return count

testcase=int(input())
while testcase:
    sum=0
    length=int(input())
    binaryIn=str(input())
    for i in range(length):
        subBinary=flipper(binaryIn,i)
        value=count1s(subBinary)
        sum+=value
    print(sum)
    testcase-=1