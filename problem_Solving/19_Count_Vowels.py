# Count Vowels  (a,e,i,o,u) 
# احسبهم داخل استرنج كام عددهم

vowels = {"a","e","i","o","u"}
count = 0 

my_string = "Hello Yousef Said From Python Can You Count The Vowels in this String".lower()

for letter in my_string:
    if letter in vowels:
        count +=1
        
print(count)        


# ans 2 

# count = sum(1 for letter in my_string if letter in vowels)

# print(count)        
