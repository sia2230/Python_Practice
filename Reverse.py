num=int(input("enter  number :"))
sum=int(0)
while(num!=0):
    temp=num%10
    sum=sum*10+temp
    num=num//10

print("reverse number is :",sum)