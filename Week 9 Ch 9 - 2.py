"""
2. Given the "julia_more_info" tuple from the book, replicated below:
    
julia_more_info = ( ("Julia", "Roberts"), (8, "October", 1967),
    "Actress", ("Atlanta", "Georgia"),
    [ ("Duplicity", 2009),
    ("Notting Hill", 1999),
    ("Pretty Woman", 1990),
    ("Erin Brockovich", 2000),
    ("Eat Pray Love", 2010),
    ("Mona Lisa Smile", 2003),
    ("Oceans Twelve", 2004) ])

write a general function that would take a tuple like this and print out a 
formatted report. The format should look like this, with the tiles and and
data:

Name:
    first_name last_name
Date of birth
    Day: D
    Month: M
    Year: Y
Place of Birth
    State: St
    City: C
Profession: value_from_tuple
Movies:
    title : year (for as many as is needed).
"""

FNAME = 0
LNAME = 1
DAY = 2
MONTH = 3
YEAR = 4
STATE = 5
CITY = 6
PROFESSION = 7
MOVIES = 8


julia = ("Julia", "Roberts", "8", "October", "1967", "Atlanta", "Georgia", "Actress", #Begin Nested tuple (don't close yet)
         
         #Enter movie and year list here
         (  ("Duplicity", 2009),     #add parenthesis for nested tuple
            ("Notting Hill", 1999),
            ("Pretty Woman", 1990),
            ("Erin Brockovich", 2000),
            ("Eat Pray Love", 2010),
            ("Mona Lisa Smile", 2003),
            ("Oceans Twelve", 2004),   
            ("Ticket to Paradise", 2022),
            ("Mirror Mirror", 2012),
        
        
         ))#end parenthesis for nested tuple


def info(person):
    print("Name:")
    print("     {} {}".format(person [0], person[1]))
    print("Date of Birth")
    print("     Day: {}" .format(person[2]))
    print("     Month: {}".format(person[3]))
    print("     Year: {}".format(person[4]))
    print("Place of Birth")
    print("     State: {}".format(person[5]))
    print("     City: {}".format(person[6]))
    print("Profession: {}".format(person[7]))
    print("Movies:")
    for movie in person[8]:
        print("     {} ({})".format(movie[0], movie[1]))

info(julia)
