import lvgl as lv
import fs_driver


# from src.utils.load_font import load_font


def main_page():

    try:
        import lib.display_driver
    except:
        pass

    # custom_font = load_font("LCD-120")
    fs_drive_letter = "S"  # Can be any letter
    fs_font_driver = lv.fs_drv_t()
    fs_driver.fs_register(fs_font_driver, fs_drive_letter)

    font = "LCD-120"

    if font == "montserrat-22":
        custom_font = lv.font_load(fs_drive_letter + ":" + "fonts/montserrat-22.bin")

    elif font == "LCD-120":
        custom_font = lv.font_load(fs_drive_letter + ":" + "fonts/LCD_Font_120.bin")

    else:
        raise ValueError(f"Font {font} is not a valid choice")

    # Column 1: fix width 60 px
    # Column 2: 1 unit from the remaining free space
    # Column 3: 2 unit from the remaining free space

    col_dsc = [lv.grid_fr(1), 175, lv.GRID_TEMPLATE.LAST]

    # Row 1: fix width 60 px
    # Row 2: 1 unit from the remaining free space
    # Row 3: fix width 60 px

    row_dsc = [lv.grid_fr(1), 100, lv.GRID_TEMPLATE.LAST]

    # Create a container with grid
    cont = lv.obj(lv.scr_act())
    cont.set_size(320, 240)
    cont.center()
    cont.set_grid_dsc_array(col_dsc, row_dsc)

    obj = []

    obj.append(lv.label(cont))
    obj.append(lv.obj(cont))
    obj.append(lv.label(cont))
    obj.append(lv.obj(cont))

    obj[0].set_grid_cell(lv.GRID_ALIGN.STRETCH, 0, 1, lv.GRID_ALIGN.STRETCH, 0, 1)
    obj[1].set_grid_cell(lv.GRID_ALIGN.STRETCH, 1, 1, lv.GRID_ALIGN.STRETCH, 0, 1)
    obj[2].set_grid_cell(lv.GRID_ALIGN.STRETCH, 0, 1, lv.GRID_ALIGN.STRETCH, 1, 1)
    obj[3].set_grid_cell(lv.GRID_ALIGN.STRETCH, 1, 1, lv.GRID_ALIGN.STRETCH, 1, 1)

    obj[0].set_style_text_color(lv.color_black(), 0)
    obj[0].set_style_text_font(lv.font_montserrat_16, 0)
    obj[0].set_text("Storage")

    obj[2].set_style_text_color(lv.color_black(), 0)
    obj[2].set_style_text_font(lv.font_montserrat_16, 0)
    obj[2].set_text("Concentrate")

    storage = lv.label(obj[1])
    storage.set_align(lv.ALIGN.CENTER)
    storage.set_style_text_color(lv.color_black(), 0)
    storage.set_style_text_font(custom_font, 0)
    storage.set_text("80")

    concentrate = lv.label(obj[3])
    concentrate.set_align(lv.ALIGN.CENTER)
    concentrate.set_style_text_color(lv.color_black(), 0)
    concentrate.set_style_text_font(custom_font, 0)
    concentrate.set_text("25")

    return (storage, concentrate)
