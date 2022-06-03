def add_time(start, duration, weekday=False):
    start_time_data = start.split()
    start_time = start_time_data[0].split(':')  # returns a tuple (' https://www.w3schools.com/python/ref_string_partition.asp ')
    start_hours = int(start_time[0])
    start_min = int(start_time[1])
    start_am_pm = start_time_data[1]

    duration_items = duration.split(":")
    duration_hours = int(duration_items[0])
    duration_min = int(duration_items[1])

    # AM_PM Flip Dictionary:
    am_pm_dict = {'AM': 'PM', 'PM': 'AM'}

    # Weekday Dictionary:
    weekday_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    # Minutes:
    minutes = start_min + duration_min

    if minutes >= 60:
        minutes = minutes - 60
        duration_hours += 1

    if minutes < 9:
        minutes = f'0{minutes}'

    # Hours:
    total_hours = start_hours + duration_hours
    hours = total_hours % 12

    if hours == 0:
        hours = 12

    # AM_PM:
    am_pm = start_am_pm
    am_pm_periods = int(total_hours / 12)

    if am_pm_periods % 2 != 0:
        am_pm = am_pm_dict.get(start_am_pm)

    # Days:
    days = int(duration_hours / 24)
    output_days = ""

    if start_am_pm == 'PM' and am_pm == 'AM':
        days += 1

    if days == 1:
        output_days = " (next day)"
    elif days > 1:
        output_days = f' ({days} days later)'

    # Weekday:
    output_weekday = ""

    if weekday:
        weekday = weekday.lower().capitalize()
        search_value_weekday = (weekday_dict.get(weekday) + days) % 7

        for key, value in weekday_dict.items():
            if search_value_weekday == value:
                output_weekday = f', {key}'

    new_time = f'{hours}:{minutes} {am_pm}{output_weekday}{output_days}'

    return new_time
