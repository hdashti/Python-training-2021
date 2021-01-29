def my_sum(*args):
    result = 0
    for i in args:
        result = result + i
    return result

val = my_sum(10, 20,49, 4)
print(val)