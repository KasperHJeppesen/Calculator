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

#4 calculator options    
def calculate(n1, n2):
    multiple = n1 + n2 
    print("Multiple gives the values:", multiple)
    
    minus = n1 - n2
    print("Minus gives the values:", minus)
    
    add = n1 * n2
    print("Add gives the values:", add)
    
    devide = n1 / n2
    print("devide gives the values:", devide)

calculate(values_first, values_second)


