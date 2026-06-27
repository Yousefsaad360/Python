#Remove Duplicates
#مع الحفاظ على الترتيب.

my_list = [1,2,2,2,3,3,5,5,1,1]

result = []

for num in my_list:
    if num not in result:
        result.append(num)
        
print(result)
        
            
     
    