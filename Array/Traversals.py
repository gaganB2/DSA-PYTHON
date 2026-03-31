arr = [3,7,2,9,4]
# Maximum Value
max_value = arr[0]
for i in arr:
    if i>max_value:
        max_value = i
print(max_value)

# Minimum Value
minimumvalue = arr[0]
for comparingnumbers in arr:
    if comparingnumbers < minimumvalue:
        minimumvalue = comparingnumbers
print(minimumvalue)

#Sum of Array
total = 0
for numbers in arr:
    total += numbers
print(f"Sum of Array : {total}")

arrayeven = [1,2,3,4,6]
count = 0
for numbers in arrayeven:
    if numbers % 2 == 0:
        count +=1
print("Total even numbers in ", arrayeven, " is = ", count) 