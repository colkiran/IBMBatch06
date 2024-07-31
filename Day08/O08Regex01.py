
import re

st = "hello world"
print(f"st :{st}")

# check if the string starts with hello
# match - function to regex, r'' - raw string

# res = re.match(r'^hello', st)

# match will work only at the begning of the string
res = re.search(r'world$', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")

