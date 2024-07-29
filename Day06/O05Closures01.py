
def outerFun(gname):
    gnm = "Mr." + gname
    def innerFun():

        print("Hello World")
        print(f"Greetings {gnm}")

    return innerFun

inRef = outerFun("Rahul")

st = "the quick brown fox jumps over the lazy dog"

res1 = [word for word in st.split()]
print(res1)

res2 = [(word, len(word)) for word in st.split()]
print(res2)

print(st[::-1])

print("-" * 60)

# after few lines of code we are calling the innerFun
inRef()





# -------------------

# print("-" * 60)
#
# def multiplyMe(x, y):
#     return x * y
#
# res = multiplyMe(20, 10)
# print(f"res :{res}")
#
#
#
#
#
#

