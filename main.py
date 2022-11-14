from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != 'exit':
    user_input = input(user_input_message)  # User input
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    print(type(days_and_unit_dict))
    validate_and_execute(days_and_unit_dict)


"""
    user_input = input('\nPlease input your number of days and desired conversion --> \n')  # User input
    print(type(user_input.split(", ")))
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_list in user_input.split(", "):
        validate_and_execute() 
"""


