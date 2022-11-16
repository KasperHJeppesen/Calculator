from unicodedata import decimal

#Print start text
starttext = 'Now, this is a calculator. You need to enter your values'
print(starttext)

#Promt the user for two inputs
values_one = float(input('enter your number: '))
values_two = float(input('enter your number: '))

#We need the + or -
while True: 
    sign = input('Enter your sign')

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
    print("Multiple gives the value:", multiple)
    
    minus = t1 - t2
    print("Minus gives the value:", minus)
    
    add = t1 * t2
    print("Add gives the value:", add)
    
    devide = t1 / t2
    print("devide gives the value:", devide)

calculate(values_one, values_two)


