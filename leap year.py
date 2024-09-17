b=float(input("Enter the year"))
a=int(b)
if a>0:
    if(a%400==0) or (a%4==0):
        print("It is Leap year")
    elif a%4==1:
            print("It is Not a Leap year")
            print("the last leap year is:",a-1)
            print("the next leap year is:",a+3)
    elif a%4==2:
        print("not  a leap year")
        print("the last leap year is:",a-2)
        print("the next leap year is:",a+2)
    elif a%4==3:
        print("It is Not a Leap year")
        print("the last leap year is:",a-3)
        print("the next leap year is:",a+1)
else:
    print("year cannot be 0 or negative")
    
        
