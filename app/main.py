from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivmob import KivMob, TestIds

class QuickAdApp(App):
    def build(self):
        self.ads = KivMob(TestIds.APP)

        self.ads.new_banner(TestIds.BANNER)
        self.ads.request_banner()

        self.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.ads.request_interstitial()

        try:
            self.ads.new_rewarded(TestIds.REWARDED)
            self.ads.request_rewarded()
        except:
            pass

        root = BoxLayout(orientation='vertical', padding=16, spacing=12)
        root.add_widget(Label(text="Demo AdMob complet", size_hint=(1,0.15)))

        b1 = Button(text="Afficher bannière")
        b1.bind(on_release=lambda *_: self.ads.show_banner())
        root.add_widget(b1)

        b2 = Button(text="Cacher bannière")
        b2.bind(on_release=lambda *_: self.ads.hide_banner())
        root.add_widget(b2)

        b3 = Button(text="Afficher interstitiel")
        b3.bind(on_release=lambda *_: self.show_inter())
        root.add_widget(b3)

        b4 = Button(text="Afficher rewarded")
        b4.bind(on_release=lambda *_: self.show_reward())
        root.add_widget(b4)

        return root

    def show_inter(self):
        try:
            self.ads.show_interstitial()
            self.ads.request_interstitial()
        except:
            pass

    def show_reward(self):
        try:
            self.ads.show_rewarded()
            self.ads.request_rewarded()
        except:
            pass

if __name__ == "__main__":
    QuickAdApp().run()
    
