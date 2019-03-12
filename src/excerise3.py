total = 0
count = 0
numbers = list()

while True:
    number1 = input('enter number: ')

    if number1 == 'done':
        break
    try:
        number1 = int(number1)
        numbers.append(number1)
    except:
        print('Invalid Input')

for number1 in numbers:
    total = total + number1
    count = count + 1


average = total/count
print('total', total)
print('count',count)
print('ave', average)
