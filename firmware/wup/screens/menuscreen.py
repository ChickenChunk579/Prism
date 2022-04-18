import pyglet
import os
import wup
import datetime
import subprocess
import imgui.integrations.pyglet as pygletimgui
import imgui
joysticks = pyglet.input.get_joysticks()
assert joysticks, 'No joystick device is connected'
joystick = joysticks[0]

show = False
window = None
wupPaths = []
label = None
label1 = None
label2 = None
renderer =  None
buttons = []
background_sprite = None

def init(window):
    global background_sprite, label, label1, label2
    window = window
    label = pyglet.text.Label("Hello!",
                            font_name="monospace",
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x='center', anchor_y='center')

    label1 = pyglet.text.Label("We are happy to see you here!",
                            font_name="monospace",
                            font_size=36,
                            x=window.width//2, y=window.height//2 - 40,
                            anchor_x='center', anchor_y='center')

    label1 = pyglet.text.Label("Press A to continue",
                            font_name="monospace",
                            font_size=36,
                            x=window.width//2, y=window.height//2 - 80,
                            anchor_x='center', anchor_y='center')


    label2 = pyglet.text.Label("System menu and firmware is all made by ChickenChunk. Using only open source software!",
                            font_name="monospace",
                            font_size=20,
                            x=25, y=25)

    background = pyglet.image.load("./wup/assets/bg.jpeg")
    background_sprite = pyglet.sprite.Sprite(background)
    getWupPaths()
    buttonWindowInit()
    
def update(dt):
   
    if show and os.path.exists("./save/00000000/hasBeenOpened"):
        
        background_sprite.draw()
        title = pyglet.text.Label("Prism Menu",
                                font_name="monospace",
                                font_size=36,
                                x=0, y=0)
        title.draw()
        openButtonWindow()
        clockWindow()
        volumeWindow()
        imgui.render()
        renderer.render(imgui.get_draw_data())


        
    elif show:
        label.draw()
        label1.draw()
        label2.draw()
        if joystick.buttons[0]:
            open("./save/00000000/hasBeenOpened", "w").write("probably shouldn't delete me XD lol sussy baka amogus")

def testclick():
    print("test button clicked")
    exit()

def on_mouse_press(x,y,button,modifiers):
    for btn in buttons:
        btn.on_mouse_press(x,y,button,modifiers)

def openButtonWindow():
    # start new frame context
    imgui.new_frame()
    imgui.begin("Games / Apps", True)

    createWupButtons()


    imgui.end()

def buttonWindowInit():
    global renderer
    imgui.create_context()
    renderer = pygletimgui.create_renderer(window)

def getWupPaths():
    for filepath in os.listdir("./titles"):
        if filepath.endswith(".wup"):
            wupPaths.append(filepath)

def createWupButtons():
    for filepath in wupPaths:
        manifest = wup.load_wup_manifest("./titles/" + filepath)
        if imgui.button(manifest["displayName"]):
            wup.execute_wup("./titles/" + filepath)

def clockWindow():
    imgui.begin("Clock")
    imgui.text(datetime.datetime.now().strftime("%H:%M"))
    imgui.end()

def volumeWindow():
    imgui.begin("Volume")

    value = 0

    changed, value = imgui.slider_float("Volume", value, 0, 100)

    if changed:
        os.system(f"amixer -D pulse sset Master {int(value)}%")

    imgui.end()