#  if...else Statement

# if
number = int(input('Enter a number: '))

if number > 0:
    print(f'The number {number} is positive')

# -----------------------------------------------------

# if..else

number = int(input('Enter a number: '))

if number > 0:
    print(f'The number {number} is positive')
else:
    print(f'The number {number} is not positive')

# -----------------------------------------------------

# if...elif...else

grade = int(input('Enter your marks for grades: '))

if grade >= 90:
    print("A+")
elif grade >= 80:
        print("A")
elif grade>=70:
        print("B")
elif grade>=60:
         print("C")
elif grade>=50:
          print("D")
else:
          print("F")

# -----------------------------------------------------

# nested if Statements

number = 5

if number >= 0:
    if number == 0:
        print(f'The number {number} is zero')
    else:
        print(f'The number {number} is positive')
else:
    print("Number is Negative")        

# -----------------------------------------------------
