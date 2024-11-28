# take input from the user
number=int(input("please enter the number: "))

#store the original number for comparision
original_number=number
revers_number=0

#revers the number
while number > 0:
    digit=number % 10
    revers_number=revers_number*10 + digit
    number //=10
    
#check if the number and revers number are same or not
if original_number == revers_number:
    print(f"{original_number} is a palindrome")
else :
    print(f"{original_number} is not a palindrome")