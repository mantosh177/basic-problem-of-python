# Question- search for a number x in this tuple using loop:
#tup= (1,4,2,5,6,7,77,88,99,56,100)

nums= (1,4,2,5,6,7,77,88,99,56,7,100) 
x=7
i = 0 
while i<len(nums):
    if(nums[i]==x):
        print("FOUND at index ",i)
    else:
        print("finding....")
    i+=1
