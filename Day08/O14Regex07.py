# {n, m}

import re

st = "baaaaaat"
print(f"st :{st}")

res = re.search(r'ba{3, 6}t', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


