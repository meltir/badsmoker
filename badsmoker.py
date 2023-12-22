from microbit import *
import music

count = 0
set_volume(64)

while True:
    if button_a.was_pressed():
        display.show(Image.SAD)
        speaker.on()
        count -= button_a.get_presses()
        music.play(music.POWER_DOWN)
    if button_b.was_pressed():
        display.show(Image.HAPPY)
        speaker.on()
        count += button_b.get_presses()
        music.play(music.POWER_UP)
    speaker.off()
    sleep(1000)
    display.scroll('Points: ')
    display.scroll(count)
    
