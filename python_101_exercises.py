# 1. Hello, you!

name = input('What is your name? ')
print('Hello ' + name + '! How are you today!')

# ------------------------#

# 2. HELLO, YOU!

# name = input('What is your name? ').upper()
# length = len(name)
# print('HELLO ' + name + '! ' + ' YOUR NAME HAS ' + str(length) + ' LETTERS IN IT!' )
# print('HELLO %s! YOUR NAME HAS %s LETTERS IN IT!' % (name, length))

#-------------------------#

# 3. Madlib
# print('Please fill in the blanks below: ___(name)___\'s favorite ___(subject)___ in school. ')
# name = input('Enter a name ').upper()
# subject = input(name + '\'s' + ' favorite school subject? ').upper()
# print('%s\'s favorite subject in school is %s.' % (name, subject))

#-------------------------#

# 4. Day of the Week

# day = input('Day (0-6)? ')
# if day == "0":
#     print('Sunday')
# elif day == "1":
#     print('Monday')
# elif day == "2":
#     print('Tuesday')
# elif day == "3":
#     print('Wednesday')
# elif day == "4":
#     print('Thursday')
# elif day == "5":
#     print('Friday')
# elif day == "6":
#     print('Saturday')
# else:
#     print('Please enter a number 0-6')

#-------------------------#

# 5. Work or Sleep In?

# day = int(input('Day (0-6)? '))
# if day == 0 or day == 6:
#   print('Sleep In')
# elif day >= 1 and day <= 5:
#   print('Work')
# else:
#   print('Please enter a number 0-6')

#-------------------------#

# 6. Celsius to Fahrenheit

# degrees = input('Temperature in Celsius? ')
# fahrenheit = int(degrees) * 1.8 + 32
# print(f)

#-------------------------#

# 7. Tip Calculator
# bill_total = int(input('How much was your bill? '))
# service = input('How was your service? good, fair, or bad? ').lower()
# if service == 'good':
#     tip_amount = bill_total * 0.2
# elif service == 'fair':
#     tip_amount = bill_total * 0.15
# elif service == 'bad':
#     tip_amount = bill_total * 0.1
# else:
#     print('Please indicate service as good, fair, or bad.')
# total = bill_total + tip_amount
# print('Tip Amount: ${:.2f}'.format(tip_amount))
# print('Tip Amount $' + str(tip_amount))
# print(f'Tip Amount ${tip_amount}')
# print(f'Tip Amount $ %s' % (tip_amount))
# print('Your Total is ${:.2f}'.format(total))

#-------------------------#

# 8. Tip Calculator 2

bill_total = float(input('How much was your bill? '))
service = input('How was your service? good, fair, or bad? ')
split = int(input('How many way are you splitting check? '))

if service == 'good':
    tip_amount = bill_total * 0.2
elif service == 'fair':
    tip_amount = bill_total * 0.15
elif service == 'bad':
    tip_amount = bill_total * 0.1
else:
    print('Please indicate service as good, fair, or bad.')

total = bill_total + tip_amount
split_total = total / split
print('Tip Amount: ${:.2f}'.format(tip_amount))
print('Your Total is ${:.2f}'.format(total))
print('Your Total each is ${:.2f}'.format(split_total))

#-------------------------#

# 9. 1 to 10

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

#-------------------------#

# 10. How many coins?
# coins = 0
# print(f'You have {coins} coins.')
# user_input = input('Do you want another? ')
# while user_input == 'yes':
#     coins += 1
#     print(f'You have now {coins} coins.')
#     user_input = input('Do you want another? ')
#     if user_input == 'no':
#         break
