
def outerFun(gname):
    gnm = "Mr." + gname
    def innerFun():

        print("Hello World")
        print(f"Greetings {gnm}")

    innerFun()

outerFun("Rahul")
