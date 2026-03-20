#nested if else

num = int(input("enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print("positive and even")
    else:
        print("positive but odd")
else:
    print("negative number")