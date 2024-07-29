"""
if a function is taking another as an argument or returning a function as reference then we call it as HOF - Higher Order Function
"""
def outerFun(greet):        # HOF

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
KanTiger = KanGrt("tiger")
KanTiger("Prabhakar")


"""
EngGrt = outerFun("Welcome")
ESngArw = EngGrt("----->")
KanGrt = outerFun("Namaskara")
KDblArw = KanGrt("=====>>")

ESngArw("Sachin")

KDblArw("Rahul")
"""
