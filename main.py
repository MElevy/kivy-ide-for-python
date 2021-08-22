from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
class mainApp(App):
	def exec_code(self, code):
		import sys
		import io
		old_stdout=sys.stdout
		new_stdout=io.StringIO()
		sys.stdout=new_stdout
		try:
			exec(code)
		except Exception as e:
			print(e)
		result=new_stdout.getvalue()
		sys.stdout=old_stdout
		return result
if __name__=='__main__':
	mainApp().run()