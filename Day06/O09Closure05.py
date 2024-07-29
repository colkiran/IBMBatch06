
def fun(*args):
    print(args)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
print("-" * 60)


def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def outerFun(fnc):          # HOF
    def innerFun(*args):
        print("Logging into the service.....")
        print(fnc(*args))              # callback
        print("-" * 60)

    return innerFun

addRef = outerFun(sum)
addRef(20, 10)

diffRef = outerFun(diff)
diffRef(78, 36)
