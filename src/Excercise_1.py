str = input('Enter a string: ')
str = str.strip()

length = len(str)

#davis
#01234
#length = 5

#leng = length - 1

while True:
    if str == 'done':
        break;
    length = length - 1
    print(str[length])

#sivad
#43210
