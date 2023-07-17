import re
import pyperclip


# 实时检测粘贴板数据
def watch_clipboard():
    while True:
        clipboard_text = pyperclip.paste()  # 获取粘贴板中的文本
        processed_text = re.sub(r'[\r\n]+', ' ', clipboard_text)  # 将换行符替换为空格

        # 替换粘贴板中的文本
        if processed_text != clipboard_text:
            pyperclip.copy(processed_text)

        # 继续监听粘贴板
        pyperclip.waitForNewPaste()


# 运行程序
if __name__ == "__main__":
    print("Will remove all \\n in clipboard")
    watch_clipboard()
