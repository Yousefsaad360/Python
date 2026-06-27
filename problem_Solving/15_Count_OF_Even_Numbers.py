#Count Even Numbers
#أعطى المستخدم List من الأرقام.
# احسب عدد الأرقام الزوجية.

my_list = [12,15,20,20,30]

count = 0

for num in my_list:
    if num % 2 == 0 :
        count +=1


print(count)