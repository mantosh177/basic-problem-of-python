# wap to print sum of first n numbers 
n = int(input("enter a number:"))
sum =0
# for i in range(1,7):
#     sum+=i
#using while loop 
i=1
while i<=n:
    sum+=i
    i+=1


print("toal sum is : ",sum)