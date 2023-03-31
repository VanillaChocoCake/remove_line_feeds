import re
import pyperclip
import time
pre_content = content = pyperclip.paste()
print("Will remove all \\n")
while True:
    content = pyperclip.paste()
    if pre_content != content:
        pre_content = content
        changed = re.sub(r"\s{2,}", " ", pre_content)
        pyperclip.copy(changed)
        time.sleep(0.1)
