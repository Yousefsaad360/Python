#أدخل رقمًا واحسب مجموع أرقامه.
#Ex
# Input: 1234
# Output: 10

#MY Answer

the_number = input("Please Enter The Number of Digit")
result = 0
i = 0 
while i < len(the_number):
    result = result +int(the_number[i] ) 
    i += 1
    
print(result)   
        


# Chat Gpt Answer 

# n = int(input())

# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10

# print(total)

