# اكتب برنامج يجيب ثاني أكبر رقم مختلف.
# بدون استخدام sort() 

my_list = [100,200,300,777,-100,-44,9,0,30]

largest = float("-inf")
second_large = float("-inf")

for num in my_list:
    if num > largest:
        second_large = largest
        largest = num 
    elif num > second_large and num != largest:
        second_large = num    
        
print(second_large)        
