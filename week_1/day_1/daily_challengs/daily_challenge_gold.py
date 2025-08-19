from datetime import datetime

# Ask for birthdate
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
birth_date = datetime.strptime(birthdate, "%d/%m/%Y")

# Calculate age
today = datetime.now()
age = today.year - birth_date.year
if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
    age -= 1

# Get number of candles (last digit of age)
candles = age % 10

# Create cake
cake = f"""       ___{"i" * candles}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~"""

# Display cake
print(cake)

# Bonus: If leap year, show second cake
if birth_date.year % 4 == 0 and (birth_date.year % 100 != 0 or birth_date.year % 400 == 0):
    print("\nBonus cake for leap year!")
    print(cake)

