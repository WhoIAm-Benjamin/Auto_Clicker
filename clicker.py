# coding: utf8

# for logging of program
import logging

# for work with system
import os
import pyautogui, keyboard
from pynput import mouse

# for waiting in program
from time import sleep

# for design
# noinspection PyUnresolvedReferences
from PySide2 import QtCore, QtGui, QtWidgets
import design


logging.basicConfig(level = logging.DEBUG,
				   format = '%(asctime)s : %(levelname)s : %(message)s',
				   filename = 'logs.log',
				   filemode = 'w'
				   )

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
	""" App for work """
	def __init__(self):
		# open access to variables in file design.py
		super().__init__()
		self.setupUi(self)

		# buttons
		self.capturePicture.clicked.connect(self.capture_picture_click())
		self.captureScope.clicked.connect(self.capture_scope_click)
		self.startButton.clicked.connect(self.start_program)
		self.stopButton.clicked.connect(self.stop_program)
		self.exitButton.clicked.connect(self.exit_program)

	def capture_picture_click(self):
		pass

	def capture_scope_click(self):
		pass

	def start_program(self):
		pass

	def stop_program(self):
		pass

	def exit_program(self):
		pass

i = 1
x = 0
y = 0
x1 = 0
y1 = 0


# noinspection PyShadowingNames,PyUnusedLocal
def on_click(x, y, button, pressed):
	global i
	if pressed:
		if button == 'left':
			if i == 1:
				x, y = x, y
				i += 1
			elif i == 2:
				x1, y1 = x, y
	if not pressed:
		# Stop listener
		return False

# noinspection PyShadowingNames
def hotkey(source, source_0, reg):
	""" hotkey for pause process
	source: source of picture
	source_0: source of main window
	req: region of search
	:param source: source of picture;
	:param source_0: source of main window;
	:param reg: region of screen for search;
	"""
	logging.debug('def "hotkey"')
	print('\rPAUSE					', end = '')
	logging.debug('PAUSE')
	while True:
		if keyboard.is_pressed('+'):
			logging.debug('Pressed "+"')
			print('\rStarted locating		 ', end = '')
			clicker(source, source_0, reg)
			break
		else:
			pass

# noinspection PyShadowingNames
def region():
	print('Click on begin region')
	with mouse.Listener(on_click=on_click) as listener:
		listener.join()
	logging.info('{}, {}'.format(x, y))
	print('Click on end region')
	with mouse.Listener(on_click=on_click) as listener:
		listener.join()
	logging.info('{}, {}'.format(x1, y1))
	region = (x, y, x1, y1)

	return region

def source():
	""" source(None):
			# return source of image
			return src """
	logging.debug('def "source"')
	print('\rDrag and drop image: ', end = '')
	src = input()
	print('\rDrag and drop window: ', end = '')
	src_0 = input()
	try:
		os.path.exists(src)
		os.path.exists(src_0)
		logging.info('File 1, file 2 exists')
	except FileExistsError:
		logging.warning('File 1 or file 2 not exists')
		source()

	logging.info('return src, src_0')
	return src, src_0


# noinspection PyShadowingNames,PyUnusedLocal
def clicker(src, src_0, reg):
	""" for locate and click on picture
	:param src: source of picture;
	:param src_0: source of main window;
	:param reg: region of screen for search;
	"""
	logging.debug('def "clicker"')
	point = None
	k = 0
	logging.info('start process')
	while point is None:
		# if pyautogui.locateOnScreen(src_0) is not None:
		print('\rNo find element		  ', end = '')
		point = pyautogui.locateCenterOnScreen(src, region = reg)
		logging.info(str(point))
		logging.debug('Element was found')
		pyautogui.moveTo(point, duration = 1)
		logging.info('Mouse was moved')
		logging.info(str(pyautogui.position()))
		pyautogui.click(point)
		logging.info('Click!')
		k += 1
		with open('count.txt', 'w') as f:
			f.write(str(k))
			logging.debug('+1 error')
		point = None
		# else:
		# 	print('\r\aNo find main window	  ', end = '')
		if keyboard.is_pressed('-'):
			logging.debug('Pressed "-"')
			hotkey(src, src_0, reg)
			keyboard.wait('*')
		elif keyboard.is_pressed('c'):
			logging.debug('Pressed "c"')
			print('\nThank\'s for you)')
			sleep(5)
			exit()

# noinspection PyShadowingNames
def main():
	""" Main window """
	logging.debug('def "main"')
	# app
	app = QtWidgets.QApplication()
	# main window of app
	window = App()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()