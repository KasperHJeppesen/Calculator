from unicodedata import decimal

#Print start text
starttext = 'Now, this is a calculator. You need to enter your values, to let the calculator do it fanzy stuff'
print(starttext)

#Promt the user for two inputs
values_first = float(input('enter your number: '))
values_second = float(input('enter your number: '))

#Failture: right sign
while True: 
    sign = input('Enter your sign ')

    if sign in ('+', '-'):
        break

#Calculate 
if sign == '+':
    c = values_first + values_second
    print("The value with multiple is", c)
else: 
    c = values_first - values_second
    print("The value with minus is", c)

#Four calculator options
def calculate(t1, t2):
    multiple = t1 + t2 
    print("Multiple gives the values:", multiple)
    
    minus = t1 - t2
    print("Minus gives the values:", minus)
    
    add = t1 * t2
    print("Add gives the values:", add)
    
    devide = t1 / t2
    print("devide gives the values:", devide)

calculate(values_first, values_second)


