#  هل الكلمه Palindrome ام لا 

# Solution 1

my_string = input("Please Enter Your word :")

if my_string == my_string[::-1]:
    print(f"{my_string} is Palindrome")
else :
    print(f"{my_string} is not Palindrome")    
    
    
# Solution 2
 
    
word = input("Enter Your Word:")

reverse = ""

for ch in word :
    reverse = ch + reverse
    
if word == reverse:
    print("This is Palindrome")
else :
    print("This isn't Palindrome")        