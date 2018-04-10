class Type:
	name = None
	extends = None
	
	def __init__(self, name, extends = None):
		self.name = name
		self.extends = extends
		
	def __str__(self):
		if self.extends == None: return "type " + self.name + ";"
		else: return "type " + self.name + " extends " + self.extends + ";"
		
	def __eq__(self, other):
		if isinstance(other, Type):
			return self.name == other.name and self.extends == other.extends
		return False
