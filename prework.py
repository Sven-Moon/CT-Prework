import math

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 
def hello_name(user_name):
  if user_name == '':
    print('Username is empty')
  else: 
    print(f'hello_{user_name.upper()}!')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
def first_odds():
  print(", ".join([str(i) for i in range(1,100,2)]))
  


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 
def max_num_in_list(a_list):  
  if isinstance(a_list, list):
    if len(a_list) == 1:
      return a_list[0]
    
    a = a_list[0]
    for i in range(1, len(a_list)):
      if a < a_list[i]:
        a = a_list[i]
    return a
  
  else: 
    print('That was not a list')
    return
    


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). 
def is_leap_year(a_year):
  if a_year % 400 == 0:
    return True
  elif a_year % 100 == 0:
    return False
  elif a_year % 4 == 0:
    return True
  else:
    return False


#Question 5
#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. 
def is_consecutive(a_list):
  if not isinstance(a_list, list):
    print('That was not a list')
    return False
    
  # Definition of consecutive assumption: Numbers that follow each other in a regular counting order, where "regular counting order" means the difference between each successive number is the same
  if len(a_list) > 3: 
    print('List too short: pattern cannot be established')
    return
  increment = a_list[0] - a_list[1]
  for i in range(1, len(a_list) - 1):
    if not math.isclose(a_list[i] - a_list[i+1], increment):
      return False
  return True