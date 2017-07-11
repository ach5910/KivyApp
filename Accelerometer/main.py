from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.label import Label 
from plyer import accelerometer
from kivy.clock import Clock 

class UI(FloatLayout):
	def __init__(self, **kwargs):
		super(UI, self).__init__(**kwargs)
		self.lblAcce = Label(text='Accelerometer: ')
		self.add_widget(self.lblAcce)
		try:
			accelerometer.enable()
			Clock.schedule_interval(self.update, 1.0/ 24)
		except:
			self.lblAcce.text = 'Failed to Start Accelerometer'

	def update(self, dt):
		txt = ""
		try:
			txt = "Accelerometer:\nX = %.2f\nY = %.2f\nZ = %.2f " % (
				accelerometer.acceleration[0],
				accelerometer.acceleration[1],
				accelerometer.acceleration[2]
				)
		except:
			txt = 'Cannot read Accelerometer!'
		self.lblAcce.text = txt 

class Accelerometer(App):
	def build(self):
		ui = UI()
		return ui
	
if __name__ = '__main__':
	Accelerometer().run()