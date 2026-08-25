# -*- coding: utf-8 -*-
import re

for f in ['README.md', 'README.pt-br.md']:
    s = open(f, encoding='utf-8').read()
    before = s
    s = re.sub(r'(capsule-render\.vercel\.app/api\?[^)\s]*?)%26', r'\g<1>%2B', s)
    if s != before:
        open(f, 'w', encoding='utf-8', newline='').write(s)
        print(f, 'corrigido')
    else:
        print(f, 'sem mudanca')
