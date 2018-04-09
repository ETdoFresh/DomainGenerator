from random import randrange
from random import choice
import uuid
from Type import Type
from Object import Object
from Property import Property
from copy import copy
from Operation import Operation

actions = []
objects = []
properties = []
types = []

unusedTypes = []
		
def GetRandomType():
	index = randrange(0, len(unusedTypes))
	typeName = unusedTypes[index]
	unusedTypes.remove(typeName)
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

def GetObjectsOfType(type):
	objectsOfType = []
	for object in domainObjects:
		if object.type == type:
			objectsOfType.append(object)
	return objectsOfType
	
def GetRandomOperation(property):
	objectsOfType = GetObjectsOfType(property.returnType)
	if (len(objectsOfType) < 1):
		return None
	
	operation = choice(['=', '!='])
	object = objectsOfType[randrange(0, len(objectsOfType))]
	return Operation(property, operation, object)
	

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

t1 = Type("Test1")
t2 = Type("Test1")
print (t1 == t2)

for i in range(0, 3):
	unusedTypes = copy(types)
	domainTypes = []
	domainObjects = []
	domainProperties = []
	domainInitialSet = []
	domainActions = []
	
	for j in range(0, randrange(1,5)):
		domainTypes.append(GetRandomType())
	
	for j in range(0, randrange(1,5)):
		domainObjects.append(GetRandomObject(domainTypes))
			
	for j in range(0, randrange(1,5)):
		domainProperties.append(GetRandomProperties(domainTypes))
		
	max = 1
	if (len(domainProperties) > 1): max = randrange(1, len(domainProperties))
	for j in range(0, max):
		property = domainProperties[j]
		operation = GetRandomOperation(property)
		if (property != None):
			domainInitialSet.append(operation)
					
	print("domain: \"" + str(uuid.uuid4()) + "\"")
	
	for type in domainTypes:
		print(type)
		
	for object in domainObjects:
		print(object)
		
	for property in domainProperties:
		print(property)
		
	for initialState in domainInitialSet:
		print(initialState)
		
	print()
