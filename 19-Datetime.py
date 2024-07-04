import datetime

print("----->Datetime<-----")
print("\n")

print("Dates:")
x = datetime.datetime.now()
print(x)
print("\n")

print("Date Output:")
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print("\n")

print("Creating Date Objects:")
x = datetime.datetime(2020, 5, 17)

print(x)
print("\n")

print("strftime() Method:")
x = datetime.datetime(2018, 6, 1)

print("Weekday, short version:",x.strftime("%B"))
print("Weekday, full version:",x.strftime("%a"))
print("Weekday as a number 0-6, 0 is Sunday:",x.strftime("%A"))
print("Day of month 01-31:",x.strftime("%w"))
print("Month name, short version:",x.strftime("%d"))
print("Month name, full version:",x.strftime("%b"))
print("Month as a number 01-12:",x.strftime("%m"))
print("Year, short version, without century:",x.strftime("%y"))
print("	Year, full version:",x.strftime("%Y"))
print("Hour 00-23:",x.strftime("%H"))
print("Hour 00-12:",x.strftime("%I"))
print("AM/PM:",x.strftime("%p"))
print("Minute 00-59:",x.strftime("%M"))
print("Second 00-59:",x.strftime("%S"))
print("Microsecond 000000-999999:",x.strftime("%f"))
print("UTC offset:",x.strftime("%z"))
print("Timezone:",x.strftime("%Z"))
print("Day number of year 001-366:",x.strftime("%j"))
print("Week number of year, Sunday as the first day of week, 00-53:",x.strftime("%U"))
print("Week number of year, Monday as the first day of week, 00-53:",x.strftime("%W"))
print("Local version of date and time:",x.strftime("%c"))
print("	Century:",x.strftime("%C"))
print("Local version of date:",x.strftime("%x"))
print("Local version of time:",x.strftime("%X"))
print("A % character:",x.strftime("%%"))
print("ISO 8601 year:",x.strftime("%G"))
print("ISO 8601 weekday (1-7):",x.strftime("%u"))
print("ISO 8601 weeknumber (01-53):",x.strftime("%V"))
print("\n")
















































