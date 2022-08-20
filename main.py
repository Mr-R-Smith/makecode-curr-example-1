def on_button_pressed_a():
    if input.temperature() >= 10:
        basic.show_icon(IconNames.FABULOUS)
        music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
    else:
        basic.show_icon(IconNames.ANGRY)
        music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
input.on_button_pressed(Button.A, on_button_pressed_a)
