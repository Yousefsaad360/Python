#Largest Number
# ابحث عن أكبر رقم في List بدون استخدام: max()

my_list = [-10,0,10,20,33,40,-80,100,500]

# my_list.sort(reverse=True)
# print(my_list[0]) # اكبر رقم بعد الترتيب

largest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num
        
print(largest)    