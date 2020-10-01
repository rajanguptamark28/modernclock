from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager,Screen, SlideTransition
from kivy.uix.button import Button, ButtonBehavior
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import strftime

class ImageButton(ButtonBehavior, Image):
    pass

class StopwatchScreen(Screen):
    pass

class ClockScreen(Screen):
    pass

class MainApp(App):

    stop_watch_started = False
    stop_watch_seconds = 0

    def update(self,nap):
        if self.stop_watch_started:
            self.stop_watch_seconds += nap

        self.root.ids['clock_screen'].ids['time'].text= strftime('[b]%H[/b]:%M:%S')
        m,s = divmod(self.stop_watch_seconds,60)
        self.root.ids['stopwatchscreen'].ids['stopwatch'].text =('%02d: %02d.[size=40]%02d[/size]'% (int(m),int(s),int(s*100%100)))



    def on_start(self):
        Clock.schedule_interval(self.update,0)


    def go_forward(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction = 'left')
        screen_manager.current = 'stopwatch_screen'
         
    def go_back(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction = 'right')
        screen_manager.current = 'clock_screen'

    def start_stop(self):
        self.root.ids['stopwatchscreen'].ids['start_stop'].text='Start' if self.stop_watch_started else 'Stop'
        self.stop_watch_started = not self.stop_watch_started
    def reset(self):
        if self.stop_watch_started:
            self.root.ids['stopwatchscreen'].ids['start_stop'].text = 'Start'
            self.stop_watch_started = False
        self.stop_watch_seconds = 0


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    # LabelBase.register(name='Roboto')
MainApp().run()