input.onButtonPressed(Button.A, function () {
    if (input.temperature() >= 10) {
        basic.showIcon(IconNames.Fabulous)
        music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
    } else {
        basic.showIcon(IconNames.Angry)
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
    }
})
