

# {n}

import re

st = "baaat"
print(f"st :{st}")

res = re.search(r'ba{3}t', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


