#1
def sum_args(*args):
    return sum(args)
print(sum_args(1,2,3,4,5))

#2
def multiply_args(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_args(2,3,4))

#3
def concatenate_args(*args):
    return ''.join(str(arg) for arg in args)
print(concatenate_args("Hello", " ", "World"))

#4
def print_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
print_args_kwargs(10, 20, name="Alice", age=25)

#5
def display_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_dict(name="Bob", city="Mumbai")
