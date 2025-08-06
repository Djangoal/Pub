# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivmob import KivMob, TestIds

class MainLayout(BoxLayout):
    pass

class TestAdApp(App):
    def build(self):
        self.ads = KivMob("ca-app-pub-3940256099942544~3347511713")  # App ID de test AdMob
        self.ads.new_banner("ca-app-pub-3940256099942544/6300978111", top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()
        return MainLayout()

if __name__ == "__main__":
    TestAdApp().run()