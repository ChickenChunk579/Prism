import pyglet

class Button:
    def __init__(self, x, y, width, height, color, onclick):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.click = onclick

        self.rect = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=self.color)

    def draw(self):
        self.rect.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            print("button pressed")
            self.click()

class BorderedButton(Button):
    def __init__(self, x, y, width, height, color, border_color, onclick):
        super().__init__(x,y,width,height,color,onclick)
        self.border_color = border_color
        self.rect = pyglet.shapes.BorderedRectangle(x,y,width,height, border_color=border_color)

class TextButton(Button):
    def __init__(self, x, y, width, height, color, text, text_color, text_size, onclick):
        super().__init__(x,y,width,height,color,onclick)
        self.text = text
        self.text_color = text_color
        self.text_size = text_size

    def draw(self):
        super().draw()
        text_element = pyglet.text.Label(text=self.text, color=self.text_color, x=self.width / 2, y=self.height / 2, anchor_x="center", font_size=self.text_size, font_name="monospace")
        text_element.draw()