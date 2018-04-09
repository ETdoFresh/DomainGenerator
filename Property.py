class Property:
	name = None
	returnType = None
	parameters = None
	
	def __init__(self, name, returnType, parameters):
		self.name = name
		self.returnType = returnType
		self.parameters = parameters
		
	def __str__(self):
		output = self.returnType.name + " : " + self.name + "("
		for i in range(0, len(self.parameters)):
			parameter = self.parameters[i]
			if (i == 0): 
				output += parameter.name
			else: 
				output += ',' + parameter.name
		return output + ");"
