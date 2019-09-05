def check(li,k):
    flag=0
    if k in li:
        return True
    else:
        return False



n=int(input("Enter number of elements in list: "))

li=[]


for i in range(0,n):
    ele=int(input())
    li.append(ele)

k=int(input("Enter element to be searched for: "))

print(check(li,k))
