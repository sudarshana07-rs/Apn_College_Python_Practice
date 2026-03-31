# Swap two numbers

a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))
print(f'Befor swap: {a} and {b}')
temp=a
a=b
b=temp
print (f'After swap: {a} and {b}')
a,b=b,a
print (b,a)