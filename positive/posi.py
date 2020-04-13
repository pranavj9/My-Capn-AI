li = []
lp = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    ele=int(input())
    li.append(ele)
for i in li:
    if(i>0):
        lp.append(i)

print("Postitve numbers in the list",lp,sep=':')
