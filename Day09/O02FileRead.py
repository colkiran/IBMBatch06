
FL = open("data.txt", "r")

st = FL.read()
print(f"st :{st}")
# st = FL.read(1500)
# print(f"st :{st}")

# depending on the no of characters in a line we can mention the no of bytes
# st = FL.readline(450)
# print(st)

# st = FL.readline()
# print(st)

# st = FL.readlines(50)
# print(st)

# for line in st:
#     print(line)

FL.close()











