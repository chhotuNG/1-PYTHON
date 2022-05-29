# check given is  number perfet number or not 
p=int(input("enter number here___: "))
sum=0
for i in range(1,p):
    if p%i==0:
        sum+=i
if sum==p:
    print(f"{p} is perfect number")
else:
    print(f"{p} is not perfect number ")