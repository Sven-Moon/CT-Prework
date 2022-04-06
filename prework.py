from functools import reduce
import math

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 
def hello_name(user_name):
  """
    prints "hello_USERNAME!" USERNAME is the input of the function. 
    allows acceptance of non-string input & warns when empty is supplied
  """
  if user_name == '':
    print('Username is empty')
  else: 
    print(f'hello_{str(user_name).upper()}!')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
def first_odds():
  """prints the odd numbers from 1-100"""
  print(", ".join([str(i) for i in range(1,100,2)]))
  


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 
def max_num_in_list(a_list):  
  """return the max number of a given list; checks for non-list/tuple input"""
  if isinstance(a_list, list):
    # return only member if list only has 1
    if len(a_list) == 1:
      return a_list[0]
    
    return reduce(lambda a,b: a if a > b else b, a_list)
  
  else: 
    print('That was not a list')
    return
    


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). 
def is_leap_year(a_year):
  """returns True if the given year is a leap year else False"""
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
  """
  Returns True if all numbers in the list are consecutive numbers, else False
  -- Consecutive: Numbers that follow each other in a regular counting order, where "regular counting order" means the difference between each successive number is the same
  -- checks for non-list/tuple & non-int/float input, violation Returns False
  -- Checks for too short lists
  """
  if not isinstance(a_list, (list, tuple)):
    print('That was not a list')
    return False
    
  # Definition of consecutive assumption: Numbers that follow each other in a regular counting order, where "regular counting order" means the difference between each successive number is the same
  if len(a_list) < 3: 
    print('List too short: pattern cannot be established')
    return
  # check for 'funny' types
  for x in a_list:
    if not isinstance(x, (int,float)):
      print("Those weren't all numbers!")
      return False
  initial_increment = a_list[0] - a_list[1]
  for i in range(1, len(a_list) - 1):
    this_increment = a_list[i] - a_list[i+1]
    if not math.isclose(this_increment, initial_increment):
      return False
  return True