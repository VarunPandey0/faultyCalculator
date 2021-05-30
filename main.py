count=True
while(count):
    first_number=int(input("First number : "))
    second_number=int(input("Second number : "))
    print("Choose Opretor")
    opretor=input("('+','-','/','*'): ")
    if (first_number==45 and second_number==3) or (first_number==3 and second_number==45) and opretor=='*':
        print('result= 555')
    elif (first_number==56 and second_number==9) or(first_number==9 and second_number==56) and opretor=='+':
        print('result= 77')
    elif (first_number==56 and  second_number==6) or (first_number==6 and  second_number==56) and opretor=='/':
        print('result=4')

    else:
        if opretor=='+':
            print(f'result={first_number+second_number}')
        elif opretor=='-':
            print(f"result={first_number- second_number}")
        elif opretor=='/':
            print(f"result={first_number / second_number}")
        else :
            print(f"result={first_number*second_number}")
    continuty = input("If won't to continue enter y elae ente n : ")
    if continuty=='n':
       count=False
    else:
        continue

