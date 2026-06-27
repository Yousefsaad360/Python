#Reverse String
#Input: Ahmed
# Output: demhA

# Ans 1

my_string = "Ahmed"

print(my_string[::-1]) # demhA



# Ans 2 

name = "Yousef"

result = ""

for letter in name:
    result = letter + result
    
print(result)     # fesuoY

# Ans 3 
person = "Ahmed"

print("".join(reversed(person))) # demhA