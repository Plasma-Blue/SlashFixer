import sys
import threading
import time

import pyperclip
import pystray
import win32clipboard
import win32con
import win32gui
from PIL import Image, ImageDraw, ImageFont


__version__ == "2024.10.1"


class SlashFixer:

    def __init__(self):
        self.enabled = True
        self.icon = None
        self.flash_event = threading.Event()
        self.flash_lock = threading.Lock()
        self.exit_event = threading.Event()

    def create_image(self, text):
        image = Image.new("RGBA", (64, 64), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 50)
        except IOError:
            font = ImageFont.load_default()

        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        text_width = right - left
        text_height = bottom - top
        position = ((64 - text_width) / 2, (64 - text_height) / 2)
        draw.text(position, text, font=font, fill=(255, 255, 255, 255))
        return image

    def flash_icon(self):
        with self.flash_lock:
            original_image = self.icon.icon
            flash_image = self.create_image("\O/")

            self.icon.icon = flash_image
            self.flash_event.set()
            time.sleep(0.5)
            self.icon.icon = original_image
            self.flash_event.clear()

    def process_clipboard(self):
        if not self.enabled:
            return
        content = pyperclip.paste()
        if "\\" in content:
            new_content = content.replace("\\", "/")
            pyperclip.copy(new_content)
            print("UPDATED: ", new_content)
            self.notify_change()

    def notify_change(self):
        if not self.flash_event.is_set():
            threading.Thread(target=self.flash_icon).start()
        else:
            self.flash_event.clear()
            self.flash_event.set()

    def create_window(self):
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self.process_clipboard_message
        wc.lpszClassName = "ClipboardListener"
        wc.hInstance = win32gui.GetModuleHandle(None)
        class_atom = win32gui.RegisterClass(wc)
        return win32gui.CreateWindow(
            class_atom, "Clipboard Listener", 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None
        )

    def process_clipboard_message(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DRAWCLIPBOARD:
            self.process_clipboard()
        return 0

    def monitor_clipboard(self):
        hwnd = self.create_window()
        while True:
            try:
                win32clipboard.SetClipboardViewer(hwnd)
                break
            except:
                time.sleep(0.1)
        while not self.exit_event.is_set():
            win32gui.PumpWaitingMessages()
            time.sleep(0.1)

    def toggle_enabled(self):
        self.enabled = not self.enabled
        self.update_menu()

    def exit_app(self):
        self.exit_event.set()
        self.icon.stop()
        sys.exit(0)

    def update_menu(self):
        menu = pystray.Menu(
            pystray.MenuItem(
                "Enable" if self.enabled else "Enable",
                self.toggle_enabled,
                checked=lambda item: self.enabled,
            ),
            pystray.MenuItem("Exit", self.exit_app),
        )
        self.icon.menu = menu

    def setup_tray(self):
        image = self.create_image("\w/")
        self.icon = pystray.Icon(
            "Replace Backslash in Clipboard", image, "Replace Backslash in Clipboard"
        )
        self.update_menu()
        self.icon.run()

    def run(self):
        clipboard_thread = threading.Thread(target=self.monitor_clipboard)
        clipboard_thread.start()
        self.setup_tray()


if __name__ == "__main__":
    fixer = SlashFixer()
    fixer.run()
