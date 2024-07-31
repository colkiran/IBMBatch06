# \
# Searching for file with extension .py

import re

st = "sample.py"
print(f"st :{st}")

res = re.search(r'\.py$', st)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


