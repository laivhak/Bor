from kivy.app import App
from kivy.uix.label import Label


class BorApp(App):
    def build(self):
        return Label(text="Hello, Bor")


BorApp().run()