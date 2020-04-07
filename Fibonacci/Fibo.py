f=0
s=1
n=int(input("Enter the number of terms to be displayed:"))
if n==1:
    print(f)
elif n>=2:
    print(f,s,sep=',',end=',')
    for i in range(3,n+1):
        t=f+s
        print(t,end=',')
        f=s
        s=t
