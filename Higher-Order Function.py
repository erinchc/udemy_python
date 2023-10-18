# higher-order function:將其他function當成自己的argument

def even(num):
    return num % 2 == 0

myList = [34534, 2895, 3859, 84093, 34690]

for item in filter(even, myList):
    print(item)

