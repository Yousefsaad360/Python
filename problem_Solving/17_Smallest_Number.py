#Smalest Number
# ابحث عن اصغر رقم في List بدون استخدام: min()

my_list = [-10,0,10,20,33,40,-80,100,500]

smallest = my_list[0]

for num in my_list:
    if num < smallest:
        smallest = num
        
print(smallest)        