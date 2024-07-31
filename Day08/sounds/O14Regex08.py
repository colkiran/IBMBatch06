# []

import re

st = "bnt"
print(f"st :{st}")

# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
res = re.search(r'b[^aeiou]t', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


