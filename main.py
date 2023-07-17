import re
import pyperclip


def watch_clipboard():
    while True:
        clipboard_text = pyperclip.paste()
        processed_text = re.sub(r'[\r\n]+', ' ', clipboard_text)
        if processed_text != clipboard_text:
            pyperclip.copy(processed_text)
        pyperclip.waitForNewPaste()


if __name__ == "__main__":
    print("Will remove all \\n in clipboard")
    watch_clipboard()
