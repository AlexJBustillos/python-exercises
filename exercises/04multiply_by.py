# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(array, num ):
    multiple = []
    for each in array:
        multiple.append(each * num)
    return multiple

print(multiply_by([1, 2, 3], 5))

def multiply_by1(numbers_list, multiple):
    result = []
    for each_num in numbers_list:
        result.append(each_num * multiple)

    return result

print(multiply_by1([5, 6, 7, 3], 10))