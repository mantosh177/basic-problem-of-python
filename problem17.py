# print the elements of the following list using a loop:
#[1,3,9,16,25,36,49,64,81,100]




# ques= search for a number x in this tuple using loop


nums =(1,3,9,16,25,36,49,64,81,100,49)
x = 49
idx=0

for el in nums:
    if(el==x):
        print("number found at idx",idx )
        break
    idx+=1
