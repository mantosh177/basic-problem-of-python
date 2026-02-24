# write a recursive function to print all elements in a list. 
# hint - use list & index as parameterrs. 

def print_list(list, idx=0 ):
    if(idx== len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1)
fruits= ["mantosh ", " mango ", "anii", "apple ","banana"]



print_list(fruits)