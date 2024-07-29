
glbX = 100

def fun(x):                 # x  is a local variable
    # glbX is a glob var, we cannot assign any value to it in this line
    global glbX
    print(glbX)
    print(f"x local var :{x}")
    y = "Hello World"       # y is a local variable
    print(f"y local var :{y}")
    glbX = 250
    print(f"Inside  :{glbX}")

print(f"Before  :{glbX}")
fun(25)
print(f"After  :{glbX}")
