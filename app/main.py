# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# KivMob (AdMob wrapper pour Kivy)
from kivmob import KivMob, TestIds

class MainLayout(BoxLayout):
    pass

class QuickAdApp(App):
    def build(self):
        self.title = "QuickAdApp - Demo"
        # Initialise KivMob avec l'App ID de test
        # (Test App ID fourni par Google — ne pas oublier de changer avant publication)
        self.ads = KivMob(TestIds.APP)

        # --- Prépare les formats de test ---
        # Banner (adaptive/fixed) : on crée et demande la bannière
        self.ads.new_banner(TestIds.BANNER)      # Test banner unit
        self.ads.request_banner()

        # Interstitial : créer + préparer
        self.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.ads.request_interstitial()

        # Rewarded : créer + préparer
        # KivMob expose normalement une méthode pour rewarded ; si ta version diffère, consulte README.
        try:
            self.ads.new_rewarded(TestIds.REWARDED)
            self.ads.request_rewarded()
        except Exception:
            # Certaines versions de KivMob utilisent des noms légèrement différents.
            pass

        # UI simple
        root = BoxLayout(orientation='vertical', padding=16, spacing=12)

        root.add_widget(Label(text="Mini app demo + AdMob (test ads)", size_hint=(1, 0.15)))

        btn_show_banner = Button(text="Afficher la bannière (si non visible)", size_hint=(1, 0.12))
        btn_show_banner.bind(on_release=lambda *_: self.ads.show_banner())

        btn_hide_banner = Button(text="Cacher la bannière", size_hint=(1, 0.12))
        btn_hide_banner.bind(on_release=lambda *_: self.ads.hide_banner())

        btn_show_inter = Button(text="Afficher interstitiel", size_hint=(1, 0.12))
        btn_show_inter.bind(on_release=lambda *_: self._show_interstitial())

        btn_show_reward = Button(text="Afficher rewarded", size_hint=(1, 0.12))
        btn_show_reward.bind(on_release=lambda *_: self._show_rewarded())

        # Exemple d'action simple
        btn_dummy = Button(text="Ajouter une tâche (exemple)", size_hint=(1, 0.12))
        btn_dummy.bind(on_release=lambda *_: print("Tâche ajoutée (exemple)"))

        for w in (btn_show_banner, btn_hide_banner, btn_show_inter, btn_show_reward, btn_dummy):
            root.add_widget(w)

        return root

    def _show_interstitial(self):
        # demande et affiche si prêt
        try:
            self.ads.show_interstitial()
            # Re-request pour le prochain affichage
            self.ads.request_interstitial()
        except Exception as e:
            print("Interstitial error:", e)
            # tente de re-request
            try:
                self.ads.request_interstitial()
            except Exception:
                pass

    def _show_rewarded(self):
        try:
            self.ads.show_rewarded()
            # re-request après affichage
            self.ads.request_rewarded()
        except Exception as e:
            print("Rewarded error:", e)
            try:
                self.ads.request_rewarded()
            except Exception:
                pass

    def on_resume(self):
        # quand l'app reprend, on recharge les interstitiels/rewarded
        try:
            self.ads.request_interstitial()
            self.ads.request_rewarded()
        except Exception:
            pass

if __name__ == '__main__':
    QuickAdApp().run()
