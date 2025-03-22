import pyperclip, time

url1 = "https://www.archives.gov/files/research/jfk/releases/2025/0318/%s.pdf"
url2 = "https://github.com/7shi/jfk_files/blob/misc/jfk_text/%s.md"
url3 = "https://github.com/7shi/jfk_files/blob/misc/jfk_json/%s.json"

def waitForNewPaste(timeout=0):
    current = pyperclip.paste()
    start = time.monotonic()
    while True:
        time.sleep(0.1)
        text = pyperclip.paste()
        if text != current:
            return text
        if timeout > 0 and time.monotonic() - start > timeout:
            raise pyperclip.PyperclipTimeoutException(
                f"waitForPaste() timed out after {timeout} seconds.")

while True:
    print("Document ID?")
    id = waitForNewPaste()
    md = f"[{id}]({url1%id}) ([OCR]({url2%id})/[要約]({url3%id}))"
    print(md)
    pyperclip.copy(md)
