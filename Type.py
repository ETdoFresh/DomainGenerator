class Type:
	name = None
	extends = None
	
	def __init__(self, name, extends):
		self.name = name
		self.extends = extends

	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return "type " + self.name + ";"
		
	def __eq__(self, other):
		if isinstance(other, Type):
			return self.name == other.name and self.extends == other.extends
		return False
