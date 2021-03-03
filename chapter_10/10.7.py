while True:
    print()
    print("I will sum your two numbers.")
    print("Enter first number. (Enter 00 to quit)")
    try:
        a = int(input())
        if a == 00:
            break
        print("Enter second number. (Enter 00 to quit)")
        b = int(input())
        if a == 00:
            break
    except ValueError:
        print("Please enter the number/numbers!")
    else:
        print("The sum is:")
        print(a+b)
        print()
