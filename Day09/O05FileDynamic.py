
FL = open("data.txt", "rb")

pos = FL.seek(100, 0)
print(f"Position :{pos}")

pos = FL.seek(80, 1)
print(f"Position :{pos}")

pos = FL.seek(100, 2)
print(f"Position :{pos}")

pos = FL.seek(-100, 2)
print(f"Position :{pos}")

# pos = FL.seek(-10, 0)
# print(f"Position :{pos}")


FL.close()