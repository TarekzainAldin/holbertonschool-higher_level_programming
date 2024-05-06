#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit=abs(number)%10
if Last_digit > 5 :
    print(f"{number } is {Last_digit}greater than 5")
elif Last_digit ==0 :
    print(f"{number}  {Last_digit}]and is 0 ")
else:
    print(f"{number}  {Last_digit} and is less than 6 and not 0")