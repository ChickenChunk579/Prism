import pyglet
import threading
import time
import screens.menuscreen

show = True
window = None
label = None
boot_sprite = None

showBootIcons = True

def bootscreenThread():
    global showBootIcons
    time.sleep(5)
    showBootIcons = False
    print("boot icons should hide now")
    
    screens.menuscreen.window = window
    screens.menuscreen.show = True

isFirstFrame = True

def init():
    global label, boot_sprite
    label = pyglet.text.Label("Prismos",
                            font_name="monospace",
                            font_size=36,
                            x=window.width//2, y=window.height//2 + 100,
                            anchor_x='center', anchor_y='center')

    boot_icon: pyglet.image.Texture = pyglet.image.load("./wup/assets/boot.png")
    boot_sprite = pyglet.sprite.Sprite(boot_icon, window.width//2 - boot_icon.width // 2, window.height//2 - boot_icon.height // 2)

def update(dt):
    if show:
        global isFirstFrame
        if showBootIcons:
            boot_sprite.draw()
            label.draw()
        if isFirstFrame:
            isFirstFrame = False
            thread = threading.Thread(target=bootscreenThread)
            thread.start()