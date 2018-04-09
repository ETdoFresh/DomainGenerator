class Object:
	type = 'Untitled'
	name = 'Untitled'
	
	def __init__(self, name, type):
		self.name = name
		self.type = type
		
	def __str__(self):
		return self.type.name + " : " + self.name + ";"
