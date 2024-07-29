import random, time, sys

loans = 0

with open('careers.py', 'r') as f:
  careers_data = f.read()
careers_lines = careers_data.splitlines()
careers = {}
for line in careers_lines:
  career, salary_range = line.split(':')
  min_salary, max_salary = map(int, salary_range.split(','))
  careers[career.strip()] = (min_salary, max_salary)

with open('careers.py', 'r') as f:
  careers_data = f.read()
careers_lines = careers_data.splitlines()
career_list = []
for line in careers_lines:
  career, salary_range = line.split(':')
  career_list.append(career.strip())

def weighted_choice(items):
  weights = [i + 1 for i in range(len(items))]  # Weights increase linearly
  total_weight = sum(weights)
  choice = random.uniform(0, total_weight)
  cumulative_weight = 0
  for i, item in enumerate(items):
    cumulative_weight += weights[i]
    if choice <= cumulative_weight:
      return item

def even_range(start):
  for i in range(start, 11, 2):
    if i % 2 == 0:
      yield i 


careers_years = {
    'Registered Nurse': 4,
    'Software Developer': 4,
    'General and Operations Manager': 4,
    'Customer Service Representative': 0,
    'Accountant': 4,
    'Sales Representative': 0,
    'Office Clerk': 0,
    'Marketing Manager': 4,
    'Elementary School Teacher': 4,
    'Financial Analyst': 4,
    'Medical Assistant': 2,
    'Human Resources Specialist': 4,
    'Electrician': 4,
    'Mechanical Engineer': 4,
    'Web Developer': 4,
    'Pharmacist': 8,
    'Lawyer': 8,
    'Construction Laborer': 0,
    'Physical Therapist': 8,
    'Graphic Designer': 4,
    'Social Worker': 4,
    'Retail Salesperson': 0,
    'Administrative Assistant': 0,
    'Dental Hygienist': 4,
    'Truck Driver': 0,
    'Chef': 4,
    'Real Estate Agent': 0,
    'Police Officer': 0,
    'Registered Dietitian': 4,
    'Personal Financial Advisor': 4
}

print('You have spent the past four years navigating the halls of West Valley High School, but now, as you collect your diploma and step out into the world, the real journey begins. Welcome to the town of West Valley, where the possibilities are endless and the choices you make will shape your destiny. It\'s time to discover who you are, what you want, and how you will traverse the winding road of life ahead. The future is yours to create in this vibrant, bustling town filled with opportunities and challenges waiting to be explored. Are you ready to embark on your journey?')
input('Press enter to begin!')

print('Your first choice is which career you wish to pursue. You can change careers over time, but to start, your options are limited.')
careers_list = career_list
options = []
careers_list.reverse()
for i in range(3):
  r = weighted_choice(careers_list)
  print(f'Option {i+1}: {r}')
  careers_list.remove(r)
  options.append(r)
career = input('Which career do you choose? ')
player_career = options[int(career)-1]
print(f'You have chosen to pursue a career in {player_career}.')

print()

if careers_years[player_career] == 0:
  print('You next choice is an important one: whether or not you will go to college. Your chosen career does not require a college degree, but you may go anyway. You start with $10,000 and college costs $30,000 a year. Enter 1 to go to college, or 2 to not.')
  answer = input('Enter your choice: ')
  if answer == '1':
    college = True
  else:
    college = False
else:
  print(f'You next choice is an important one: whether or not you will go to college. Your chosen career requires {careers_years[player_career]} years. You start with $10,000 and college costs $30,000 a year. You may go to college for more years than your career requires, but it is not necessary.')
  college = True

if college:
  print('You have decided to go to college.')
  if careers_years[player_career] != 10 and careers_years[player_career] >= 2:
    range = list(even_range(careers_years[player_career]))
    range = str(range)
    range = range[1:-1]
    answer = input(f'Enter the number of years you would like to co to college ({range}): ')
    loans += int(answer) * 30000
  elif careers_years[player_career] == 10:
    print('Since your chosen career requires 10 years at college, you must go to college for 10 years.')
    loans += 300000
  else:
    print('You have decided to go to college.')
    answer = input(f'Enter the number of years you would like to co to college (2, 4, 6, 8, or 10): ')