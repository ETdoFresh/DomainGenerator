import random

class Type:
	previousTypes = []
	name = 'Untitled'
	extends = ''
	
	def __init__(self, name, extends):
		self.name = name
		self.extends = extends

	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return "type " + self.name + ";"
