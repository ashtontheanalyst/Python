import kivy

# Require the app to use this version
kivy.require('2.3.1')

# Importing specific tools from Kivy (the app base class and label from UI)
from kivy.app import App
from kivy.uix.label import Label

# Our app has to INHERIT the base class traits from Kivy's app class
class MyApp(App):

    # Build the app, initialize, and return Hello Kivy
    def build(self):
        return Label(text = "Hello Kivy")

# Once the app is fully initialized, this is what runs it
if __name__ == '__main__':
    MyApp().run()