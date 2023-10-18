a = ([1,2,3], "Wilson")
a[0][1]=100
print(a)

# if an element in a tuple is mutable, then we can just select the element, and then change it
# if we want to use a tuple as a dictionary key, then all elements in the tuple has to be immutable.


# 15
# 'Bob'
# ('Tom', [14,23,27])
# ['filename', (15,16)]
# 'filename'
# ('filename', 25, 'extension')

my_list = [3, 1, 2]
# sorted_list = sorted(my_list)
# print(sorted_list)  # Output: [1, 2, 3]
my_list.sort()
print(my_list) 

