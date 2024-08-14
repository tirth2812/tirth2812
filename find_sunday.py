import datetime
# Define a function named all_sundays that takes a year as input
def all_sundays(year):
    # Set dt to January 1st of the given year
    dt = datetime.date(year, 1, 1)
    # Move dt to the first Sunday of the given year
    dt += datetime.timedelta(days=6 - dt.weekday())  
    # Iterate through all Sundays of the given year
    while dt.year == year:
        # Yield  a result
        yield dt
        # Move to the next Sunday by adding 7 days
        dt += datetime.timedelta(days=7)
          
# Iterate through all Sundays of the year
for s in all_sundays(2024):
    # Print each Sunday
    print(s)