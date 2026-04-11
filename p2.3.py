#3  Write a program to display grade of a student based on percentage using if-elif-else.


num=int(input("Enter Your Percentage :"))

if num>= 80:
    print("You Got A Grade")
elif num>60 and num<80:
    print("You Got B Grade")
elif num>40 and num<60:
    print("You Got C Grade")
elif num<40:
    print("Fail")
else:
    print("Enter Valid Percentage")

