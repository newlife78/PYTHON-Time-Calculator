Program Description:

Program that takes in two required parameters and one optional parameter:
    . A start time in the 12-hour clock format (ending in AM or PM)
    . A duration time that indicates the number of hours and minutes
    . (optional) a starting day of the week, that is case insensitive

The program will add the duration time to the start time and return the result.

If the result will be the next day, it will show (next day) after the time.

If the result will be more than one day later, it will show (n days later) after the time, where
"n"is the number of days later.

If the program is given the optional starting day of the week parameter, then the output will
display the day of the week of the result. The day of the week in the output will appear after
the time and before the number of days later.

Below are some examples of different cases the program will handle:

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
