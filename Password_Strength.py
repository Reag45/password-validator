#Password Strength 
has_upper =False
has_digit =False
has_symbols =False
symbols= ['!','@','#','$','%','&']
#
#
#
Username= input("Enter your Username: ")
print("Password must be a minimum 12 Characters")
print("Password must contain a Uppercase Letter")
print("Password must contain a Digit")
print("Password must contain a Symbol ['!','@','#','$','%','&']")
Password= input("Enter your Password: ")

while len(Password) < 12 or has_upper == False or has_digit == False or has_symbols == False:
    has_upper = False
    has_digit = False
    has_symbols = False
    #Checks length of Password
    while len(Password) < 12:
        print("Password minimum requires 12 Characters")
        Password = input("Enter your Password: ")
    #Checks if Password contains Uppercase Characters
    while has_upper == False:
        for char in Password:
            if char.isupper():
                has_upper = True
                break
        if has_upper == False:
            print("Password must contain a Uppercase Letter")
            Password = input("Enter your Password: ")
            has_upper = False
            has_digit = False
            has_symbols = False

    while has_digit == False:
        for digit in Password:
            if digit.isdigit():
                has_digit = True
                break
        if has_digit == False:
            print("Password must contain a Digit")
            Password = input("Enter your Password: ")
            has_upper = False
            has_digit = False
            has_symbols = False

    while has_symbols == False:
        for symbol in Password:
            if symbol in symbols:
                has_symbols = True
                break
        if has_symbols == False:
            print("Password must contain a Symbol")
            Password = input("Enter your Password: ")
            has_upper = False
            has_digit = False
            has_symbols = False
#Score of Each Category
#Add additional points for the Length of password greater than the Minimum
Len_score = len(Password) - 12
Upper_score=0
Digit_score = 0
Symbols_score =0
#Add 1 Point for each Uppercase Letter in Password
for Upper_char in Password:
    if Upper_char.isupper():
        Upper_score += 1
#Add 1 Point for each Digit in Password
for Digit in Password:
    if Digit.isdigit():
        Digit_score += 1
#Add 1 Point for each Symbol in Password
for Symbol in Password:
    if Symbol in symbols:
        Symbols_score += 1

Total_Score = Len_score + Upper_score + Digit_score + Symbols_score
if Total_Score >=6:
    Score = "Strong"
elif 5>= Total_Score >=4:
    Score = "Medium"
else:
    Score = "Weak"


print(f"Welcome {Username}")
print(f"Your Password Strength is {Score}")










