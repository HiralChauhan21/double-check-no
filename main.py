num = int(input("enter the number to be checked: "))

if num>50:
    print("the number is greater than 50")
    if num%2==0 :
        print("the number is even too")
    else :
        print("the number is odd")
else :
    print("number is less than 50")