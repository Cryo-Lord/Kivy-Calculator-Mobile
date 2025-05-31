from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import get_color_from_hex as hexed #Te permite obtener el color ocupando el estandar hexadecimal Ej: "#FFFFFF"

from back_end import Mathematics
from kivy.clock import Clock
import time

class Calculator(Screen):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

        main = BoxLayout(orientation="vertical", padding="30px", spacing="15px")
        
        main.add_widget(Label(text="Calculator",size_hint_y=(0.1)))
        head = BoxLayout(size_hint_y=(0.1), spacing="10px")
        head.add_widget(Button(text="<", size_hint_x=(0.1)))

        global screenCalc
        screenCalc = TextInput(multiline=False, text="", font_size="25px", readonly=True)
        head.add_widget(screenCalc)

        def string_refresh(self):
            screenCalc.text += self.text

        def clear_string(self):
            screenCalc.foreground_color = "black"
            screenCalc.text = ""

        def calculate(self):
            calculator = Mathematics()
            print("Calculating")
            result = calculator.calculate(screenCalc.text)
            if result == "Error":
                screenCalc.foreground_color = "red"
                screenCalc.text = result
                Clock.schedule_once(clear_string, 1)
            else:
                screenCalc.text = result
            print(result)
        
        keyboard = GridLayout(cols=4, spacing="10px")
        keys = "()C/789*456-123+%0.="
        for key in keys:
            keyboard.add_widget(Button(text=key))
        for button in keyboard.children:
            if button.text == "C":
                button.bind(on_press=clear_string)
            elif button.text == "=":
                button.bind(on_press=calculate)
            else:
                print(button)
                button.bind(on_press=string_refresh)

        main.add_widget(head)
        main.add_widget(keyboard)
        self.add_widget(main)


if __name__ == "__main__":
    class TestApp(App):
        def build(self):
            self.manager = ScreenManager()
            screens = [Calculator()]
            for view in screens:
                self.manager.add_widget(view)
            return self.manager

    TestApp().run()
