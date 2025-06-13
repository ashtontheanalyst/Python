from kivy.app import App
from kivy.uix.label import Label
# New additions
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Building out our login screen to display on the app
class LoginScreen(GridLayout):

    # While we initialize the inherited grid layout class called login screen
    # We're going to overload it by adding additional things like the username, password, etc.
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

# Similar to what we did in basic.py
class MyApp(App):
    
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()