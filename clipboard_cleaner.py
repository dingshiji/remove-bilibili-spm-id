import pyperclip
import time
import re

def clean_url(url):
    cleaned_url = re.sub(r'/\?spm_id_from=.*', '/', url)
    return cleaned_url

while True:
    clipboard_content = pyperclip.paste()
    if 'https://www.bilibili.com/' in clipboard_content and '/?spm_id_from=' in clipboard_content:
        cleaned_url = clean_url(clipboard_content)
        if cleaned_url != clipboard_content:
            pyperclip.copy(cleaned_url)
            print(f'已清理剪贴板内容: {cleaned_url}')
    time.sleep(1)
