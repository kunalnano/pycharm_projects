def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif (conversion_unit == "minutes") or (conversion_unit == "mins") or (conversion_unit == "min"):
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif (conversion_unit == "seconds") or (conversion_unit == "sec") or (conversion_unit == "secs"):
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit, please use either 'hours' or 'minutes' or 'seconds'"


def validate_and_execute(days_and_unit_dict):
    try:
        user_input_int = int(days_and_unit_dict["days"])
        if user_input_int > 0:
            calculated_value = days_to_units(user_input_int, days_and_unit_dict["unit"])
            print(calculated_value)
        elif user_input_int == 0:
            print('0 is not acceptable, input a positive non-zero integer')
        else:
            print("don't be so negative man")
    except ValueError:
        print('Enter only integers or piss off')


user_input_message = "\nPlease input your number of days(key) and units(value) for desired conversion --> \n"




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


