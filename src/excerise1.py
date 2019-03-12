total = 0
count = 0

while True:
    number1 = input('enter number: ')
    if number1 == 'done':
        break
    try:
        number1 = int(number1)
        total = total + number1
        count = count + 1
    except:
        print('Invalid Input')
average = total/count
print(total)
print(count)
print(average)
