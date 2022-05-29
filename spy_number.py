
a=int(input("enter number here____: "))
sum=0
pro=1
n=str(a)
for i in n:
    sum+=int(i)
    pro*=int(i)
if sum==pro:
    print("spy number ")
else:
    print("not spy number ")