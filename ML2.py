1)
star='*'
for i in range(1,6):
    for j in range(1,i):
            print("*",end=' ')
    print("\r")
for i in range(6,1,-1):
    for j in range(1,i):
        print("*",end=' ')
    print("\r")
--------------------------------------------------------------------------
2)
myown_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in myown_list[1::2]:
    print(i,end=" ")
-------------------------------------------------------------------
3)
value = [23, 'Python', 23.98]
types = []
for i in value:
    types.append(type(i))

print(value)
print(types)
-----------------------------------------------------------------------
4)
sample_List=[1,2,3,3,3,3,4,5]
unique_List=[]
for i in sample_List:
    if i not in unique_List:
        unique_List.append(i)
print(sample_List)
print(unique_List)
---------------------------------------------------------------------
5)
def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

input_string = 'The quick Brow Fox'
upper_count, lower_count = count_case(input_string)

print("No. of Upper-case characters:", upper_count)
print("No. of Lower-case Characters:", lower_count)
--------------------------------------------------------------------
