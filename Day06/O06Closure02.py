
def outerFun(gname, flag):
    gnm = "Mr." + gname
    def innerFun1():

        print("Hello World")
        print(f"Greetings {gnm}")

    def innerFun2():

            print("Hello World")
            print(f"Hola {gnm}")

    if flag:
        return innerFun1
    else:
        return innerFun2

engGrt = outerFun("Sachin", 1)
spnGrt = outerFun("Messi", 0)
print("-" * 60)
print("-" * 60)
print("-" * 60)
engGrt()
print("-" * 60)
print("-" * 60)
print("-" * 60)
spnGrt()
print("-" * 60)
print("-" * 60)
print("-" * 60)

outerFun("Rahul", 1)()         # Calls the innerFun
print("-" * 60)
print("-" * 60)
print("-" * 60)
outerFun("Iniesta", 0)()         # calls the innerFun
