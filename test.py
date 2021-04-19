import time
import threading
import subprocess
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread
from kivy.core.window import Window


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vl = BoxLayout(orientation='vertical', padding=20)
        vl.add_widget(Image(source='img/logo.png'))
        self.input = TextInput(size_hint=(1, 0.3))
        vl.add_widget(self.input)
        btn = Button(
            text="SAVE POST",
            color='white',
            background_color=(1.0, 0.0, 0.0, 1.0),
            font_size=22,
            size_hint=(1, 0.3)
        )
        self.h1_text = Label(
            text='Enter url from Instagram and press on save post.',
            color='black',
            font_size=18
        )
        vl.add_widget(self.h1_text)
        self.progress = ProgressBar(max=99)
        vl.add_widget(self.progress)
        vl.add_widget(btn)
        self.add_widget(vl)
        btn.on_press = self.save_post

    def progress_on(self):
        for i in range(100):
            self.progress.value = i
            time.sleep(0.01)
        self.input.text = ''
        self.h1_text.text = 'Post downloaded'

    def download(self):
        url = self.input.text
        try:
            shellcode = f'instalooter post "{url}" -v store'
            result = subprocess.check_output(shellcode, shell=True)
            # print(result)
        except:
            print('Error!')

    @mainthread
    def save_post(self):
        if self.input.text.find('instagram.com') != -1:
            t1 = threading.Thread(target=self.download())
            t2 = threading.Thread(target=self.progress_on)
            t1.start()
            t2.start()
        else:
            self.h1_text.text='Error! Link is not valid!'


class MyApp(App):
    def build(self):
        Window.size = (400, 600)
        Window.clearcolor = (1, 1, 1, 1)
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        return sm


if __name__ == '__main__':
    app = MyApp()
    app.run()
