

def outerFun(gname):        # gname is a local variable

    def innerFun():
        nonlocal gname      # only local variable can be converted to nonlocal variable

        gname = 'Mr.' + gname

        print("Hello World")
        print(f"Greetings {gname}")

    # outerfun scope
    innerFun()
    print(f"gname :{gname}")
outerFun("Sachin")


