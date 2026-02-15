# write a program to print factorial of any number n 

n=int(input("enter your number :"))
factorial=1
for i in range(1,n+1):
    factorial*=i

print("The factorial is : ",factorial)

# # using while loop
# n=3
# fact=1
# i=1
# while i <=n:
#     fact*=i
#     i+=1
# print("factorial=",fact)



