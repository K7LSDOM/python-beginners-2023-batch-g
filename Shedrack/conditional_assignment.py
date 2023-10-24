X = "STARDOM MUSIC"
print(X.center(30, '^'))
print('AFROBEAT NO.1 MUSIC STREAMING PLATFORM' )
print('afroing music!!!')
print('Sign up!')
f = input("Email:")
if "@" and '.' not in f:
     
     print("email not valid, please retry.")

g = input("First name:")
h = input("Last name:")
i = input("Phone:")
j= "0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"
if  j not in i:
     print("invalid phone number")
c = input("Create Username:")
d = input("Create Password:")
if len(d)<5:
     print("Password should be at least 5 characters")
e = input("Confirm Password:")

if d==e:
    print("Get Ready! Already!")
    print("Now sign in!")
    a = input("Username:")
    b = input("Password:")
    print()

else:
     print('Incorrect username or password, please retry.')

if a==c and b==d and d==e:
     print("Listen Up!")
else:
     print("Please try again later")     
