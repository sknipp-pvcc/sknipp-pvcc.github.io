
#print("A.")
#import calendar                
#cal = calendar.TextCalendar()   # Create an instance
#cal.pryear(2012)                # What happens here?
#print("A calendar for 2012 is created")

#print("")
#print("B.-------------------------------------------------------------------------")
#import calendar
#cal = calendar.TextCalendar(firstweekday=calendar.THURSDAY)
#cal.pryear(2012)
#print("")
#print("Now the calendar starts on Thursday")

#print("")
print("C.-------------------------------------------------------------------------")
import calendar                
cal = calendar.TextCalendar()   
cal.prmonth(2023, 12)     
print('')           
print("Now only showing December")

print("")
print("D.-------------------------------------------------------------------------")
print("")
print("Spanish")
print("")
d = calendar.LocaleTextCalendar(6, "SPANISH")
d.pryear(2012)
print("")
print("Russian")
print("")
d = calendar.LocaleTextCalendar(6, "RUSSIAN")
d.pryear(2012)
print("This isn't exactly nailing cyrillic. If you actually put Русский it throws\nall kinds of errors")
print("")
print("German")
print("")
d = calendar.LocaleTextCalendar(6, "GERMAN")
d.pryear(2012)

print("")
print("E.-------------------------------------------------------------------------")
print("")
import calendar
print("Is a leap year? ")
print("2020")
print(calendar.isleap(2020))
print("2021")
print(calendar.isleap(2021))
print("2022")
print(calendar.isleap(2022))
print("2023")
print(calendar.isleap(2023))
print("2024")
print(calendar.isleap(2024))