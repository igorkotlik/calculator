def add(a, b):
    return a + b

def substract(a, b):
    return a - b

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

print("Possible operations:")
print("a. add")
print("b. substract")
operation = input("Enter operation(a/b): ")

match operation:
    case 'a':
        print(add(num_1,num_2))
    case 'b':
        print(substract(num_1,num_2))



