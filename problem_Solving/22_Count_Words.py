# Count_Words

my_string = "Hello I'm Yousef Said Elsayed Yousef".strip()

count = 0

for i in range(len(my_string)):
    if my_string[i] != " ":
        if i == 0 or my_string[i - 1] == " ":
            count += 1
            

print(count)                   
        
        