<b><Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.</b>

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data
    Invalid input
    Enter a number: 7
    Enter a number: done
    16 3 5.333333333333333

<b>Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.</b>

<b>Exercise 3: Rewrite above Exercise 1 by using while loop and for loop. Append the numbers user entered into a list variable called numbers.</b>

    ## initialization
    numbers = list()  ## numbers = []

    ## while loop
    num = input('Enter a number: ')
    num = int(num)
    numbers.append(num)

    ## for loop
    for num in numbers:
       ## write your code

<b>Exercise 4:Read an integer N. For all non-negative integers i < N, print i square(i ** 2).</b> <br>

<b>Input Format</b>
The first and only line contains the integer, .

Constraints
    
    0 < N < 21

<b>Output Format</b>

Print N lines, one corresponding to each i.

<b>Sample Input</b>

    5

<b>Sample Output</b>

    0
    1
    4
    9
    16

<b>Exercise 5:

    We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
    In the Gregorian calendar three criteria must be taken into account to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
    The year is also evenly divisible by 400. Then it is a leap year.
    This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source.</b> <br>

<b>Task</b>
You are given the year, and you have to write a function to check if the year is leap or not.<br>

Note that you have to complete the function and remaining code is given as template.

<b>Input Format</b>

Read y, the year that needs to be checked.

<b>Constraints</b>
    
    1899 < y < 100001

<b>Output Format</b>

Output is taken care of by the template. Your function must return a boolean value (True/False)

<b>Sample Input</b>

    1990

<b>Sample Output</b>

    False

<b>Explanation</b>

    1990 is not a multiple of 4 hence it's not a leap year.



<b>Coding guideline</b>

    def is_leap(year):
    leap = False
    
    # Write your logic here
    
    return leap
    
    year = int(raw_input())
    print is_leap(year)