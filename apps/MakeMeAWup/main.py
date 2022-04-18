import pyglet
window = pyglet.window.Window()
window.set_fullscreen(True)
@window.event
def on_draw():
    pyglet.gl.glClearColor(255,255,255,1)
    
    window.clear()

pyglet.app.run()