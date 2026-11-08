#count
a=int(input("Enter the number: "))
count=0
while a>0:
    count+=1
    a//=10
print(count)

n=int(input("Enter the number: "))
a=0
b=1
c=a+b
for i in range(a,n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


