#Print start text
starttext = 'This is a calculator.'
print(starttext)

#Promt the user for two inputs
values_one = float(input('Enter your first value: '))
values_two = float(input('Enter your second value: '))

#We need the + or -
while True: 
    sign = input('Enter your sign ')

    if sign in ('+', '-'):
        break

#Calculate 
if sign == '+':
    c = values_one + values_two
    print("The value with multiple is", c)
else: 
    c = values_one - values_two
    print("The value with minus is", c)

#Four calculator options
def calculate(t1, t2):
    
    multiple = t1 + t2 
    print("Multiple gives the value:", round(multiple, 2))
    
    minus = t1 - t2
    print("Minus gives the value:", round(minus, 2))
    
    add = t1 * t2
    print("Add gives the value:", round(add, 2))
    
    devide = t1 / t2
    print("Devide gives the value:", round(devide, 2))

calculate(values_one, values_two)


