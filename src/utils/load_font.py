"""/font folder must be uploaded to the esp32 via Thonny"""

import lvgl as lv
import time
import fs_driver  # important


def load_font(font: str):
    # Register file system driver
    fs_drive_letter = "S"  # Can be any letter
    fs_font_driver = lv.fs_drv_t()
    fs_driver.fs_register(fs_font_driver, fs_drive_letter)

    if font == "montserrat-22":
        custom_font = lv.font_load(fs_drive_letter + ":" + "fonts/montserrat-22.bin")

    elif font == "LCD-120":
        custom_font = lv.font_load(fs_drive_letter + ":" + "fonts/LCD_Font_120.bin")

    else:
        raise ValueError(f"Font {font} is not a valid choice")

    return custom_font
