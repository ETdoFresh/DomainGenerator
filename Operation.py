class Operation:
	property = None
	operation = None
	object = None
	
	def __init__(self, property, operation, object):
		self.property = property
		self.operation = operation
		self.object = object
		
	def __str__(self):
		output = self.property.name + "("
		for i in range(0, len(self.property.parameters)):
			parameter = self.property.parameters[i]
			if (i == 0): 
				output += parameter.name
			else: 
				output += ',' + parameter.name
		return output + ") " + self.operation + " " + self.object.name
