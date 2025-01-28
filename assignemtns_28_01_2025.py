import os

downloads_folder = os.path.expanduser("~/Downloads")

for item in os.listdir(downloads_folder):
    item_path = os.path.join(downloads_folder, item)
    if os.path.isfile(item_path):
        print(f"{item} - File")
    elif os.path.isdir(item_path):
        print(f"{item} - Folder")

import string

print(string.ascii_letters)


from random import sample
from string import ascii_letters

five_letters = ''.join(sample(ascii_letters, 5))
print(five_letters)

from datetime import timedelta,datetime
from dateutil.relativedelta import relativedelta

dt=input("enter date in dd/mm/yyyy:")
date=datetime.strptime(dt,"%d/%m/%Y")
str_date=date.strftime("%A %d %B %Y")
print(str_date)


print("Day of the input date:",date.strftime('%A'))


addedDate=date+timedelta(days=15,hours=23)
print("added 15 days and 23 hrs:",addedDate.strftime("%A %d %B %Y %H:%M"))


cur_date = datetime.now()
sixMonths = cur_date + relativedelta(months=6)
print("Date after 6 Months:", sixMonths.strftime("%A %d %B %Y"))


import random
choices = ["rock", "paper", "scissors"]

while True:

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw! Try again.")
        continue
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        break
    else:
        print("Computer wins!")
        break
