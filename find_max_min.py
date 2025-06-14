def find_max_min():
    count = 0
    while True:
        num = input("Enter Number: ")
        try:
            num = int(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    max_num = num
    min_num = num
    count += 1
    while True:
        num = input("Enter Number: ")
        if num == "":
            break
        try:
            num = int(num)
            count += 1
        except ValueError:
            print("Invalid input. Skipping.")
            continue
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f"Maximum Number is: {max_num}\n"
        f"Minimum Number is: {min_num}\n"
        f"Total valid numbers entered: {count}")
