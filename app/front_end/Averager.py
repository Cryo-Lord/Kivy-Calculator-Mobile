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
        #First row
        title = BoxLayout()
        title.add_widget(Label(text="Averager"))
        #Third row
        grades = BoxLayout(orientation="vertical")
        #Fourth row
        grades_quantity = BoxLayout()
        #Fifth row
        buttons = BoxLayout()
        #Second Row
        result = BoxLayout()
        
        order = [title, result, grades, grades_quantity, buttons]

        mainframe.add_widget(grades)
        self.add_widget(mainframe)

    def error(type:str):
        error_type = type

class TestView(App):
    def build(self):
        Manager = ScreenManager()
        Manager.add_widget(Averager(name="Averager"))
        return Manager

if __name__ == "__main__":
    TestView().run()
