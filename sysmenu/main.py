import pyglet
import screens.bootscreen
import screens.menuscreen
import pyautogui
import time
joysticks = pyglet.input.get_joysticks()
if joysticks:
    joystick = joysticks[0]
joystick.open()

window = pyglet.window.Window()
window.set_fullscreen(True)

screens.bootscreen.window = window
screens.menuscreen.window = window


# init
screens.bootscreen.init()
screens.menuscreen.init(window)

@joystick.event
def on_joyaxis_motion(joystick, axis, value):
    print("Axis: " + axis + " Value: " + str(value))
    try:
        if axis == "y":
            pyautogui.moveRel(0, value * 5, _pause=False)
        if axis == "x":
            pyautogui.moveRel(value * 5, 0, _pause=False)
    except pyautogui.FailSafeException:
        print("Failsafe")

@joystick.event
def on_joybutton_press(joystick, button):
    print("Button: " + str(button))
    if button == 0:
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        print("Clicking")


def update(dt):
    window.clear()
    screens.bootscreen.update(dt)

    screens.menuscreen.update(dt)

#window.set_mouse_visible(False)

pyglet.clock.schedule(update)

pyglet.app.run()