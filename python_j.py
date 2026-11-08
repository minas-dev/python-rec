n=int(input("Enter the number: "))
a=0
b=1
c=a+b
for i in range(a,n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
