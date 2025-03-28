import time
from src.main_page import main_page
import lvgl as lv


def main():
    (storage, concentrate) = main_page()

    s_percent = 100
    c_percent = 0

    while True:
        if s_percent < 0:
            s_percent = 100

        if c_percent > 100:
            c_percent = 0

        storage.set_text(f"{s_percent}")
        concentrate.set_text(f"{c_percent}")

        if s_percent > 75:
            storage.set_style_text_color(lv.color_hex(0xFF0000), 0)
        else:
            storage.set_style_text_color(lv.color_black(), 0)

        if c_percent < 10:
            concentrate.set_style_text_color(lv.color_hex(0xFF0000), 0)
        else:
            concentrate.set_style_text_color(lv.color_black(), 0)

        s_percent -= 7
        c_percent += 1

        time.sleep(1)


main()
