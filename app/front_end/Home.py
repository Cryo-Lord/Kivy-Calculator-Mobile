from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex as hexed #Te permite obtener el color ocupando el estandar hexadecimal Ej: "#FFFFFF"

class Menu(Screen):
    """
    Pantalla de menu para acceder a los diferentes tipos de calculadoras

    Pantalla en la cual se muestran los botones

    Problema: No se muestran los botones, tal vez GlazeWM está interfiriendo, también puede ser que la build esté
              fallando.

    Solución: El problema provenia del Buildeo, ocupando la función build no funcionaba, pero al ocupar el init
              y agregarlo asi mismo como un widget más, funciona con normalidad
    """
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        main = BoxLayout(orientation="vertical", padding="30px", spacing="15px")
        buttons = []
        fabric = ["Averager","Mathematics","Scientific","History"]
        logo = BoxLayout(spacing="5px")
        logo.add_widget(Label(size_hint_x=.2))
        logo.add_widget(Label(text="[b][color=#00bb0f]Python[/color] [color=#00ddbb]Multi[/color]-[color=#ddaabb]CalC[/color][/b]", markup=True, font_size="50sp", outline_width="3px", size_hint=(.8,1)))

        main.add_widget(logo)

        for product in fabric:
            ensambling = Button(text=product, background_normal="", background_color= hexed("#aadd00"))
            buttons.append(ensambling)
        for button in buttons:
            main.add_widget(button)
        self.add_widget(main)

if __name__ == "__main__":
    class TestApp(App):
        """
        Esquema para probar las pantallas, su unico proposito es montar las pantallas screenmanager
        Solución para el aspect ratio: colocar una imagen de background, fijarla en el aspect ratio; cualquier cosa 
        que lo tenga de fondo se adaptará a esa imagen
        """
        def build(self):
            Window.clearcolor = hexed("#888888")
            self.main = ScreenManager()
            screens = [Menu()]
            for screen in screens:
                self.main.add_widget(screen)
            return self.main

    TestApp().run()
