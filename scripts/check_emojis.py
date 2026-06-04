import re
from pathlib import Path
t = Path(r'c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html').read_text(encoding='utf-8')
em = re.findall(r'[\U0001F300-\U0001FAFF\U00002700-\U000027BF]+', t)
print('lines', t.count('\n')+1)
print('emojis', len(em), em[:5])
print('empty span logos', len(re.findall(r'int-card-logo"><span></span>', t)))
print('detail-brand-mark count', t.count('detail-brand-mark'))
print('brand-mark count', t.count('brand-mark'))
