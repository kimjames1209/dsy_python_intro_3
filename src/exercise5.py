def is_leap(year):
    leap = False

    if year >=1900:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap = True
    # Write your logic here
    return leap

year = int(raw_input())
print (is_leap(year))
