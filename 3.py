choice = int(input("Enter your choice (1-4):\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n"))

match choice:
    case 1:
        print("Add")
    case 2:
        print("Subtract")
    case 3:
        print("Multiply")
    case 4:
        print("Divide")
    case _:
        print("Invalid Choice")
