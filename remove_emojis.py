import re

file_path = r"c:\Arcnio proj\presentation.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

emojis = ['🏭 ', '📅 ', '💡 ', '📷 ', '🦾 ', '🖥️ ', '📊 ', '✅ ', '🟢', '✅', '🏭', '📅', '💡', '📷', '🦾', '🖥️', '📊']
for e in emojis:
    content = content.replace(e, '')

# Replace any empty checkmark spans
content = content.replace('<span class="check"></span>', '<span class="check">✓</span>')

# Remove footer from Slide 2
footer_regex = re.compile(r'<div class="footer-note">\s*<div class="dot"></div>\s*All 3 systems communicate via HTTP API — single source of truth\s*</div>', re.MULTILINE)
content = footer_regex.sub('', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully cleaned the HTML")
