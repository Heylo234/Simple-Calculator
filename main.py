for i in range(100):
    sign = input("What calculation should I do?(e.g subtraction, addition)")
    first = input("First Number>")
    second = input("Second Number>")
    if sign == "addition":
        print("sum:")
        print(int(first) + int(second))
    else:
        if sign == "subtraction":
            print("difference:")
            print(int(first) - int(second))
        else:
            if sign == "multiplication":
                print("product:")
                print(int(first) * int(second))
            else:
                if sign == "division":
                    print("quotient:")
                    print(int(first) / int(second))
                else:
                    print("Something when wrong! Try again.")
