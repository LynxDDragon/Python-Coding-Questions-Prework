#Coding Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the
#function. The first line of code has been defined as below.

def hello_name(user_name):
    print(f"Hello_{user_name}") 

#note to self: remember to remention the function name 
hello_name('Bryan')

#Coding Question 2
#Write a python function, first_odds that prints odd numbers from 1-100 and
#returns nothing

def first_odds():
    for odd_numbers in range(1,100):
        if odd_numbers % 2 != 0:
            print(odd_numbers, end=" ")
first_odds()

#Question 3
#Please write a Python function, max_num_list to return a max number of a given
#list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[0]
    for number in a_list:
        if number > max:
            max = number
    return max
a_list= [1,25,37, 5, 3]
print (max_num_in_list(a_list))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is
#divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
         return True
    elif (a_year % 100 == 0) and (a_year % 400 == 0):
         return True
    else:
         return False
print (is_leap_year(2024))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
# consecutive numbers. The return should be boolean Type.

def consecutive(b_list):
    if len(b_list)< 1:
        return False

    max_val = max(b_list)
    min_val = min(b_list)

    if max_val - min_val + 1 == len(b_list):
        return True
    else:
        return False

b_list= [9, 10, 11, 13, 12]
print (consecutive(b_list))
        # consecutive number formula is n+1
