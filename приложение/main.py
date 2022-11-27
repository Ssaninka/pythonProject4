from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.lang import Builder

from kivy.core.window import Window
Window.size=(480,800)

kv = Builder.load_file('ui.kv')

class TapeScreen(Screen):
    pass

class FavouritesScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass
class TestApp(App):


    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(TapeScreen(name='tape'))
        sm.add_widget(FavouritesScreen(name='favourites'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()