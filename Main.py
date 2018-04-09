from random import randrange
import uuid
from Type import Type
from Object import Object
from Property import Property

actions = []
objects = []
properties = []
types = []
		
def GetRandomType():
	index = randrange(0, len(types))
	return Type(types[index])

def GetRandomObject(types):
	typeIndex = randrange(0, len(types))
	objectIndex = randrange(0, len(objects))
	return Object(objects[objectIndex], types[typeIndex])

def GetRandomProperties(types):
	propertyTypes = []
	for i in range(0, randrange(1, 4)):
		typeIndex = randrange(0, len(types))
		propertyTypes.append(types[typeIndex])
	
	typeIndex = randrange(0, len(types))
	returnType = types[typeIndex]
	
	propertyIndex = randrange(0, len(properties))
	propertyName = properties[propertyIndex]
	
	return Property(propertyName, returnType, propertyTypes)
	

# -- MAIN -----------------------------------------
path = 'data/'

with open(path + 'actions.txt', 'r') as file:
	actions = file.read().splitlines();
	
with open(path + 'objects.txt', 'r') as file:
	objects = file.read().splitlines();

with open(path + 'properties.txt', 'r') as file:
	properties = file.read().splitlines();

with open(path + 'types.txt', 'r') as file:
	types = file.read().splitlines();


for i in range(0, 3):
	domainTypes = []
	domainObjects = []
	domainProperties = []
	domainActions = []
	
	for j in range(0, randrange(1,5)):
		domainTypes.append(GetRandomType())
	
	for j in range(0, randrange(1,5)):
		domainObjects.append(GetRandomObject(domainTypes))
			
	for j in range(0, randrange(1,5)):
		domainProperties.append(GetRandomProperties(domainTypes))
					
	print("domain: \"" + str(uuid.uuid4()) + "\"")
	
	for type in domainTypes:
		print(type)
		
	for object in domainObjects:
		print(object)
		
	for property in domainProperties:
		print(property)
		
	print()
