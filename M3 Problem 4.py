# This program will tell you what day of the week you will return.
print("Days of the week: 0 through 6",
      "where 0 is Sunday and day 6 is Saturday")
print("When are you leaving?")
starting_day_string = input()
starting_day_int = int(starting_day_string)
print(starting_day_int)

print("How many days are you leaving for?")
returning_day_string = input()
returning_day_int = int(returning_day_string)
print(returning_day_int)

returning_day = starting_day_int + returning_day_int

print("You will come back on day: ", returning_day % 6)