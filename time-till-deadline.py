from _datetime import datetime
import django

user_input = input("Enter your goal with deadline date in format (mm.dd.yyyy), separated by colon\n")
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%m.%d.%Y")
today_date = datetime.today()

# calculate how many days from now is the deadline
days_till = deadline_date - today_date
hours_till = int(days_till.total_seconds() / 60 / 60)

print(f"Dear user, time remaining for your goal {goal} is {days_till.days} days\n")
print(f"Dear user, time remaining for your goal {goal} is {hours_till} hours\n")
