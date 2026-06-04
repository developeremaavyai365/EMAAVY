import re
p = r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html"
with open(p, encoding="utf-8") as f:
    s = f.read()
idx = s.find("section>iv")
print("BROKEN:", repr(s[idx - 120 : idx + 80]))
idx2 = s.find("dropdown-section-title")
while idx2 >= 0:
    chunk = s[idx2 : idx2 + 600]
    if "Telephony" in chunk:
        print("DROPDOWN:", chunk[:700])
        break
    idx2 = s.find("dropdown-section-title", idx2 + 1)
