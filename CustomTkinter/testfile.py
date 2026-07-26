from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout

# Set window size (for testing)
Window.size = (350, 600)

KV = '''
ScreenManager:
    HomeScreen:
    PasswordGeneratorScreen:

<HomeScreen>:
    name: "home"

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)
        padding: dp(10)

        # Top User Greeting
        MDLabel:
            text: "Hello, Kev"
            font_style: "H6"
            halign: "left"
            theme_text_color: "Primary"

        # Search Bar
        MDTextField:
            hint_text: "Search"
            icon_right: "magnify"
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}

        # Recent Saved Section
        MDLabel:
            text: "Recent Saved"
            font_style: "Subtitle1"
            halign: "left"
            theme_text_color: "Secondary"
            padding: [10, 5]

        ScrollView:
            MDList:
                id: recent_list

        # Bottom Navigation Bar
        MDBottomAppBar:
            MDToolbar:
                icon: "plus"
                type: "bottom"
                left_action_items: [["home", lambda x: app.switch_screen("home")]]
                right_action_items: [["cog", lambda x: app.switch_screen("password")]]
                mode: "end"

<PasswordGeneratorScreen>:
    name: "password"

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)
        padding: dp(10)

        MDLabel:
            text: "Password Generator"
            font_style: "H6"
            halign: "center"

        MDTextField:
            hint_text: "Generated Password"
            icon_right: "content-copy"
            readonly: True
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}

        MDSlider:
            min: 6
            max: 32
            value: 16
            hint: True

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(10)

            MDSwitch:
                id: uppercase_switch
                text: "Include Uppercase"
            MDSwitch:
                id: numbers_switch
                text: "Include Numbers"
            MDSwitch:
                id: symbols_switch
                text: "Include Symbols"

        MDRaisedButton:
            text: "Generate Password"
            pos_hint: {"center_x": 0.5}
            on_release: app.generate_password()

        MDFloatingActionButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen("home")
'''

# Kivy App Class
class PasswordApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # Match the UI color
        return Builder.load_string(KV)

    def switch_screen(self, screen_name):
        self.root.current = screen_name

    def generate_password(self):
        import random
        import string

        length = 16  # Fixed length (You can adjust based on slider value)
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"

        password = ''.join(random.choice(chars) for _ in range(length))

        self.root.get_screen("password").ids['password_field'].text = password

# Run the App
if __name__ == "__main__":
    PasswordApp().run()
