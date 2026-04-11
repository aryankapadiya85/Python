#5.  Write a program to demonstrate the use of break statement.

a=[6,8,9,5,17]
val= 10

for i in a:
    if i == val:
        print(f"Found at {i}")
        break
else:
    print("Value not Found")
