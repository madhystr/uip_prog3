from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder

traduc = {
	"abeja": "bee",
	"abejaguila": "eagle",
	"araña": "spider",
	"ardilla": "squirrel",
	"ballena": "whale",
	"burro": "donkey",
	"caballo": "horse",
	"cabra": "goat",
	"camello": "camel",
	"canguro": "kangaroo",
	"caraco": "snail",
	"cebra": "zebra",
	"cisne":"swan",
	"coala": "koala",
	"cocodrilo": "crocodile",
	"conejo": "rabbit",
	"cordero": "lamb",
	"elefante": "elephant",
	"gallina": "hen",
	"ganso": "goose",
	"gato": "cat",
	"hipopótamo": "hippopotamus",
	"hormiga": "ant",
	"hornero": "baker",
	"insecto": "insect",
	"jirafa": "giraffe",
	"langosta": "crab",
	"leon": "lion",
	"lobo": "wolf",
	"luciernaga": "firefly",
	"mariposa": "butterfly", "mono": "monkey", "mosquito": "mosquito", "oso": "bear", "pajaro": "bird", "paloma": "dove", "pantera": "panther", "pato": "duck", "pavo": "turkey",
				"perro": "dog", "pez": "fish", "pinguino": "penguin", "pulpo": "octopus", "rana": "frog", "rata": "rat", "rinoceronte": "rhinoceros", "serpiente": "snake", "tigre": "tiger", "vaca": "cow",
				"zorro": "fox"}


class PrincipalScreen(Screen):
	def Traducir(self):
		palabra = self.ids['nom1'].text
		print('--------------------------------')
		print(palabra)
		print('--------------------------------')
		for esp, ing in traduc.items():
			print(esp)
			if esp in palabra:
				self.ids['nom2'].text=ing
				break

class TraductorApp(App):
	def build(self):
		pantalla = ScreenManager()
		pantalla.add_widget(PrincipalScreen(name = 'principal'))
		return pantalla

if __name__ == '__main__':
	TraductorApp().run()
