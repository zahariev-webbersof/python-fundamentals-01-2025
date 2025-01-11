# 🖼️ Python Pattern Drawing Project

Welcome to the **Python Pattern Drawing Project**! 🎉 This project is designed to help you understand and implement nested loops, conditional statements, and user inputs in Python.

---

## 📝 Project Overview

Your task is to create various patterns using Python's printing capabilities. You'll build a program where users can choose from different patterns, provide necessary inputs, and see the results displayed in the terminal. 

---

## 🎯 Objectives

- Practice working with **nested loops**.
- Use **if-elif-else conditions** to implement logic.
- Handle **user input** to create dynamic patterns.
- Understand **alignment** using spaces and characters.

---

## 🚀 Patterns to Implement

1️⃣ **Right-angled Triangle**  
```
*
**
***
****
*****
```

2️⃣ **Square with Hollow Center**  
```
*****
*   *
*   *
*   *
*****
```

3️⃣ **Diamond**  
```
  *
 ***
*****
 ***
  *
```

4️⃣ **Left-angled Triangle**  
```
****
***
**
*
```

5️⃣ **Hollow Square**  
```
******
*    *
*    *
*    *
*    *
******
```

6️⃣ **Pyramid**  
```
   *
  ***
 *****
*******
```

7️⃣ **Reverse Pyramid** (New!)  
```
*******
 *****
  ***
   *
```

8️⃣ **Rectangle with Hollow Center** (New!)  
```
********
*      *
*      *
********
```

---

## 📋 Instructions

1️⃣ **Run the Program**  
Start the program and choose a pattern from the menu.  

2️⃣ **Input Dimensions**  
Provide necessary inputs (e.g., number of rows or size of the shape).  

3️⃣ **See the Result**  
Enjoy the output directly in your terminal.  

4️⃣ **Try Again!**  
You can run the program again to explore different patterns.  

---

## 🛠️ Code Skeleton

Below is the **skeleton code** with comments to guide you through the implementation. Your task is to fill in the missing parts and complete the program!

```python
# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input(Fore.LIGHTWHITE_EX + "Enter the number corresponding to your choice: "))

rows = 0
size = 0

quit_message = False

while not quit_message:

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5, 9]:  # removed choice 8 since it doesn't need size
        size = int(input("Enter the size of the figure: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        for row in range(1, rows + 1):
            color = ''
            if row % 2 == 0:
                color = f'{Fore.LIGHTRED_EX + chr(64 + row)} '
            else:
                color = f'{Fore.LIGHTBLUE_EX + chr(64 + row)} '
            print(color * row)

        """
        # a more basic solutions, w/o colors and letters:
        char = '*'
        for row in range(1, rows + 1):
            print(char * row)

        # or a solution w/ nested loops:
        char = '*'
        for row in range(1, rows + 1):
            for _ in range(row):
                print(char, end='')
            print()
        """

    elif choice == 2:  # Square with Hollow Center
        for s in range(1, size + 1):
            color = Fore.LIGHTMAGENTA_EX + '*  '
            # for the figure to look like a square rather than a rectangle,
            # there should be two extra spaces after the star,
            space = '   '  # and each 'space' needs to be three spaces long
            if s == 1 or s == size:
                print(color * size)
            else:
                print(f'{color}{(size - 2) * space}{color}')


    elif choice == 3:  # Diamond
        half_rows = int(rows / 2)
        color = ''
        space = '   '  # I think the extra spaces make a better looking diamond :)
        if rows % 2 == 0:
            for row in range(1, rows + 1):
                color = Fore.LIGHTGREEN_EX + ' $ '
                if row <= half_rows:
                    print(f"{(half_rows - row) * space}{color * (row + row - 1)}")
            for row in range(half_rows, -1, -1):
                color = Fore.LIGHTRED_EX + ' $ '
                print(f"{(half_rows - row) * space}{color * (row + row - 1)}")
        else:
            for row in range(1, rows + 1):
                if row < half_rows + 1:
                    color = Fore.RED + ' $ '
                    print(f"{(half_rows + 1 - row) * space}{color * (row + row - 1)}")
                elif row == half_rows + 1:
                    color = Fore.LIGHTYELLOW_EX + ' $ '
                    print(f"{(half_rows + 1 - row) * space}{color * (row + row - 1)}")
            for row in range(half_rows, -1, -1):
                color = Fore.GREEN + ' $ '
                print(f"{(half_rows + 1 - row) * space}{color * (row + row - 1)}")


    elif choice == 4:  # Left-angled Triangle
        for row in range(rows, -1, -1):
            if rows % 2 == 0:
                if row % 2 != 0:
                    print('♥️' * row)
                else:
                    print('♠️' * row)
            else:
                if row % 2 != 0:
                    print('♦️️' * row)
                else:
                    print('♣️️' * row)

    elif choice == 5:  # Hollow Square
        for s in range(1, size + 1):
            char = '😜 '
            # for the figure to look like a square rather than a rectangle,
            # there should be two extra spaces after the star,
            space = '🫥 '  # and each 'space' needs to be three spaces long
            if s == 1 or s == size:
                print(char * size)
            else:
                print(f'{char}{(size - 2) * space}{char}')

    elif choice == 6:  # Christmas Pyramid
        for row in range(rows):
            char1 = '  '
            if row == 0:
                char2 = Fore.LIGHTYELLOW_EX + '* '
            elif row % 2 != 0:
                char2 = Fore.LIGHTGREEN_EX + '* '
            else:
                char2 = Fore.LIGHTRED_EX + '* '
            print(char1 * (rows - (row + 1)), end='')
            print(char2 * (row + 1), end='')
            print(char2 * row)

    elif choice == 7:  # Reverse Pyramid
        char1 = '  '
        char2 = Fore.LIGHTYELLOW_EX + '* '
        for row in range(rows - 1, -1, -1):
            print(char1 * (rows - (row + 1)), end='')
            print(char2 * (row + 1), end='')
            print(char2 * row)

    elif choice == 8:  # Rectangle with Hollow Center
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        char1 = Fore.CYAN + '*  '
        char2 = '   '
        for h in range(1, height + 1):
            if h == 1 or h == height:
                print(width * char1)
            else:
                print(f'{char1}{(width - 2) * char2}{char1}')

    elif choice == 9:  # Butterfly - an additional pattern
        char1 = Fore.LIGHTRED_EX + '* '
        char2 = '  '
        char3 = Fore.LIGHTYELLOW_EX + '* '
        for num in range(1, size):
            print(char3, end='')
            print((num - 1) * char1, end="")
            print(char2 * (2 * (size - num)), end="")
            print((num - 1) * char1, end='')
            print(char3)
        for num in range(size, 0, -1):
            print(num * char1, end="")
            print(char2 * (2 * (size - num)), end="")
            print(num * char1)

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Optional - Allow the user to restart or exit
    choice = int(input(Fore.LIGHTWHITE_EX + "Enter the number corresponding to your choice or enter 0 to quit: "))
    if choice == 0:
        quit_message = True

---

## 🏁 Conclusion

By completing this project, you'll:
- Master nested loops to create complex patterns. 🌀
- Understand how to manipulate text alignment in Python. 📐
- Get hands-on experience with user inputs and conditional logic. 💻

This is a great stepping stone towards becoming proficient in Python programming. Enjoy your journey and have fun coding! 🚀

---

## 🌟 Bonus Ideas

- Add more patterns like spirals, checkerboards, or alphabets.  
- Enhance the program to allow saving patterns as text files.  
- Add color to the output using libraries like `colorama`.  
