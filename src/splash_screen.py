import lvgl as lv


def splash(scr):
    # Create a label for the splash screen
    label = lv.label(scr)
    label.set_text("Loading...")
    label.center()

    # clear the splash screen
