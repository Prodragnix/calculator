def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b
print('Please select the operation: ')
print('a.Add')
print('b.Subtract')
print('c.Multiply')
print('d.Divide')
choice=input('Enter your option here: ')
num1=int(input('Please enter your first number: '))
num2=int(input('Please enter your second number: '))
if choice=='a':
    print(add(num1,num2))
elif choice=='b':
    print(minus(num1,num2))
elif choice=='c':
    print(divide(num1,num2))
elif choice=='d':
    print(multiply(num1,num2))
else:
    print('Please enter a valid option.')