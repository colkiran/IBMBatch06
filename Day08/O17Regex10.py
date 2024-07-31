import re

lno = "LCNO-KAR-72-2021-9000"
print(f"lno :{lno}")

res = re.search(r'LCNO-(KAR|KER|ANP|TlG|TND)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', lno)

if res:
    print("Match found...")
    print(res.group(0))         # the string that matched the regex
else:
    print("Match not found...")


#\d