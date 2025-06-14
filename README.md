# Find Maximum, Minimum, and Count of Inputs

This is a simple Python program that:

- Accepts multiple number inputs from the user
- Ignores invalid (non-numeric) inputs
- Finds the *maximum* and *minimum* numbers
- Counts the total number of *valid entries*
- Stops accepting input when the user presses *Enter without typing anything*

## 🔧 How It Works

1. The program starts by asking for a valid integer.
2. After the first valid number, it enters a loop to accept more inputs.
3. Input ends when the user presses *Enter* on an empty line.
4. It then returns:
   - The highest number entered
   - The lowest number entered
   - The number of valid entries

## 📄 Code Example

```python
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

