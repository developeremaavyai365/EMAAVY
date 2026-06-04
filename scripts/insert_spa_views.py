from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from patch_spa_main import build_spa_views

FILE = Path(__file__).resolve().parent.parent / 'emaavy_white_blue (2).html'
text = FILE.read_text(encoding='utf-8')

old = '    </footer>\n  </div>\n\n\n  <div class="detail-drawer"'
if old not in text:
    raise SystemExit('marker not found')

new = '''    </footer>
  </div>
  </div>
''' + build_spa_views() + '''
  </div>

  <div id="site-footer-root"></div>

  <div class="detail-drawer"'''

text = text.replace(old, new, 1)
FILE.write_text(text, encoding='utf-8')
print('OK - inserted', text.count('spa-view'), 'spa-view references')
