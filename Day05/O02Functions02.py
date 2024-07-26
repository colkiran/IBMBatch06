
from collections import  namedtuple

def Results(hltktNo):
    GS = 95
    SS = 90
    MT = 97
    L1 = 75
    L2 = 80
    nmdTpl = namedtuple("Marks", "sc st ma l1 l2")
    marks = nmdTpl(sc=GS, st=SS, ma=MT, l1=L1, l2=L2)
    return marks

mrks = Results(12009)
print(mrks)
print(f"Science :{mrks.sc}")
print(f"Social  :{mrks.st}")
print(f"Maths   :{mrks.ma}")
print(f"Lang-1  :{mrks.l1}")
print(f"Lang-2  :{mrks.l2}")




# immutable tuple or creating a class using functions