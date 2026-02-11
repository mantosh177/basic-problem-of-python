# Question = Grade students based on marks 
#marks >=90 , grade= "A"
#90> marks>=80, grade= "B"
#80> marks >=70 , grade = "C "
# 70>marks, grade = " D "

marks = int(input("Enter the marks : "))
if(marks>= 90):
    print("grade = A ")
elif(90> marks>=80):
    print("grade = B ")
elif(80>marks >=70 ):
    print("grade = C ")
else:
    if(0<marks <70):
        print("Need to improve.")

    
# marks =int( input("Enter marks of the student : "))

# if(marks >= 90):
#     grade = "A"
# elif(marks>= 80 and  marks <90):
#     grade= "B"
# elif(marks >=70 and marks <80):
#     grade= "C"
# else:
#     grade = "D"
# print("grade of the student :", grade )