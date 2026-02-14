
# Question  - Write a program to enter marks of 3 subjects from the user and store them in a dictionary.

# start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}

x= int(input("Enter phy : "))
marks.update({"phy" : x})
y = int(input("Enter che : " ))
marks.update({"che ": y } )
z= int(input("Enter math : " ))
marks.update({"math": z})
print(marks)