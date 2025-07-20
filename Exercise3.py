while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))
        if 1 <= number <= 10:
            print("Thank you!")
            break
        else:
            print("Number out of range. Try again.")
    except ValueError:
        print("Please enter a whole number between 1 and 10.")
