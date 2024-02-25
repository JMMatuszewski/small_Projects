import datetime, random

BIRTHDAYSNUMBER = 25
CYCLESNUMBER = 100000

def getBirthdays(numberOfBirthdays):
    """Create pull of birthdays from 2001.01.01"""

    startingDate = datetime.date(2001,1,1)
    birthdays = []

    for i in range(numberOfBirthdays):
        birthday = startingDate + datetime.timedelta(random.randint(0,364))
        birthdays.append(birthday)

    return birthdays


def getMatch(birthdays):
    """Check for repeating date"""

    if len(birthdays) == len(set(birthdays)):
        return False #Wszystkie daty są unikatowe

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return True

#INTRO
print('''
Paradox of birthday shows, that in group of N people there is a chance,
that two persons will have birthday on the same day, that is surprisingly high.
This program uses Monte Carlo method (repeatable random simulations) to determine 
the probability.

(In reality it's not a paradox, just surprisingly high outcome.)
''')

#Start of symulation
matchAmount = 0
for i in range(CYCLESNUMBER):
    if i % 10000 == 0:
        print("{} cycles has passed...".format(i))

    birthdays = getBirthdays(BIRTHDAYSNUMBER)
    if getMatch(birthdays):
        matchAmount += 1

# Show results of the simulation
probability = round(matchAmount / CYCLESNUMBER * 100, 5)
print("In simulation with {} cycles for {} people,".format(CYCLESNUMBER,BIRTHDAYSNUMBER))
print("repeating birthdays has occured {} times,".format(matchAmount))
print("which gives us {}% probability.".format(probability))


    


