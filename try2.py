# a = 10

# def change(num):
#     # num = a (copy by value) => num = 10
#     num = 25

# change(a)
# print(a)

a = [1,2,3,4]

def change(lst):
    # lst = a (copy by reference) => lst = a
    lst[0]=100  # a = [100, 2, 3, 4]

change(a)
print(a)

