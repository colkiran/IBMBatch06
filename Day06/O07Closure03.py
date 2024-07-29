
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

# we can create greet in a necessary language - we can greet many players

EngGrt = outerFun("Welcome")
SpnsGrt = outerFun("Hola")

print("-" * 60)
EngGrt("Sachin")
EngGrt("Rahul")
EngGrt("Sourav")
EngGrt("Virat")

print("-" * 60)
SpnsGrt("Messi")
SpnsGrt("Ronaldo")
SpnsGrt("Iniesta")
SpnsGrt("Xavi")
