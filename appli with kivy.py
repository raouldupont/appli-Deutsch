import kivy
from kivy.app import App
from kivy.uix.boxlayout import Boxlayout


kivy.require("2.0.0")

class GameView(Boxlayout):
    def __init__(self):
        super(GameView,self).__init()
        
        
class Raoulapp(App):        
    def build(self):
        return GameView()

new = Raoulapp()
Raoulapp.run