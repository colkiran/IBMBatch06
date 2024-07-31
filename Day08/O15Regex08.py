# ()

import re

st = "bait"
print(f"st :{st}")

res = re.search(r'b(ai|es)t', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


