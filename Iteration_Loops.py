state = False
largest_num = None
smallest_num = None
num_list = []

while state == False:
    
    userinp = input("Enter Number: ")

    if userinp == "done":
        state = True
        break

    try:
        userinp = int(userinp)

    except:
        print("Invalid input")
        continue
    
    num_list.append(userinp)

for num in num_list:
    if largest_num is None:
        largest_num = num

    elif num > largest_num:
        largest_num = num

for num in num_list:
    if smallest_num is None:
        smallest_num = num

    elif num < smallest_num:
        smallest_num = num

print("Maximum is", largest_num)
print("Minimum is", smallest_num)