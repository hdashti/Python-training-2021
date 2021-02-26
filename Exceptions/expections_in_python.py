def open_file(fname):
    with open(fname, 'r') as f:
        print(f.read())


try:
    lst = [1, 2]
    print(lst[10])
    open_file("./test.txt")
    num = 1 / 0

except FileNotFoundError:
    print("FileNotFoundError : something went wrong")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:  # finally will execute in any condition
    print("finally")

print("after try")
