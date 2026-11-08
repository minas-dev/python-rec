
# reverse a number
r=int(input("enter the number to reverse: "))
d=0
while r>0:
    dig=r%10
    d=d*10+dig
    r//=10
print(d)



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

