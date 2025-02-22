from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup

class Averager(Screen):
    #UI
    def __init__(self, **kwargs):
        super(Averager, self).__init__(**kwargs)
        mainframe = BoxLayout(orientation="vertical")
        title = BoxLayout(Label(text="Averager"))
        grades = BoxLayout(orientation="vertical")
        grades_quantity = BoxLayou()
        buttons = BoxLayout()
        result = BoxLayout()
    
    def error(type:str):
        error_type = type

class TestView(App)
    def build(self):
        Manager = ScreenManager()
        Manager.add_widget(Averager(name="Averager"))

if __name__ == "__main__":
    TestView().run()
