
# +

import re

st = "baaaaaaaaaaaaaaaaaaat"
print(f"st :{st}")

res = re.search(r'ba+t', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


