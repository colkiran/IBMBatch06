
class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass


age = 4
try:
    if age < 6:
        raise TooTiny("Too very young to vote.......")
    elif age < 18:
        raise TooYoung("Young and still not eligible to vote....")
    elif age > 100:
        raise TooOld("Too very old to cast a vote......")
except TooTiny as t:
    print(t)
except TooYoung as y:
    print(y)
except TooOld as o:
    print(o)
else:
    print("You can cast your valuable vote.....")
finally:
    print("completed the process of voting....")






