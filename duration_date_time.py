import datetime

now = datetime.datetime.now()

# create a timedelta object for 1 day

one_day = datetime.timedelta(days=1)  #timedelta == class is used to determine duration between two dates or time
#syntex===timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# add the timedelta object to the current date and time

next_day = now + one_day

# print the current date and time and the next day

print("Current Date and Time:", now)

print("Next Day:",next_day)