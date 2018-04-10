from random import randrange
from random import choice
from random import getrandbits
import uuid
from Type import Type
from Object import Object
from Property import Property
from copy import copy
from Operation import Operation

MinAmountOfTypes, MaxAmountOfTypes = 1, 5
MinAmountOfObjects, MaxAmountOfObjects = 1, 5
MinAmountOfProperties, MaxAmountOfProperties = 1, 5
MinAmountOfAuthorGoals, MaxAmountOfAuthorGoals = 1, 5
MinLengthOfAuthorGoal, MaxLengthOfAuthorGoal = 1, 3

actions = []
objects = []
properties = []
types = []

unusedTypes = []
		
def SafeRandomRange(x, y):
	if (x == y): return x
	if (x > y): return randrange(y, x)
	else: return randrange(x, y)

def GetRandomType(domainTypes, unusedTypes):
	index = SafeRandomRange(0, len(unusedTypes))
	typeName = unusedTypes[index]
	unusedTypes.remove(typeName)
	if bool(getrandbits(1)) or len(domainTypes) == 0:
		return Type(typeName)

	index = SafeRandomRange(0, len(domainTypes))
	extends = domainTypes[index]
	return Type(typeName, extends.name)

def GetRandomObject(types):
	typeIndex = SafeRandomRange(0, len(types))
	objectIndex = SafeRandomRange(0, len(objects))
	return Object(objects[objectIndex], types[typeIndex])

def GetRandomProperties(types):
	propertyTypes = []
	for i in range(0, SafeRandomRange(1, 4)):
		typeIndex = SafeRandomRange(0, len(types))
		propertyTypes.append(types[typeIndex])
	
	typeIndex = SafeRandomRange(0, len(types))
	returnType = types[typeIndex]
	
	propertyIndex = SafeRandomRange(0, len(properties))
	propertyName = properties[propertyIndex]
	
	return Property(propertyName, returnType, propertyTypes)

def GetObjectsOfType(type, objects):
	objectsOfType = []
	for object in objects:
		if object.type == type:
			objectsOfType.append(object)
	return objectsOfType
	
def GetRandomOperation(property, objects):
	objectsOfType = GetObjectsOfType(property.returnType, objects)
	if (len(objectsOfType) < 1):
		return None
	
	operation = choice(['=', '!='])
	object = objectsOfType[SafeRandomRange(0, len(objectsOfType))]
	return Operation(property, operation, object)

def Main():
	unusedTypes = copy(types)
	domainTypes = []
	domainObjects = []
	domainProperties = []
	domainInitialSet = []
	domainAuthorGoals = ''
	domainActions = []
	
	for i in range(0, SafeRandomRange(MinAmountOfTypes, MaxAmountOfTypes)):
		domainTypes.append(GetRandomType(domainTypes, unusedTypes))
	
	for i in range(0, SafeRandomRange(MinAmountOfObjects, MaxAmountOfObjects)):
		domainObjects.append(GetRandomObject(domainTypes))
			
	for i in range(0, SafeRandomRange(MinAmountOfProperties, MaxAmountOfProperties)):
		domainProperties.append(GetRandomProperties(domainTypes))
		
	for i in range(0, SafeRandomRange(1, len(domainProperties))):
		property = domainProperties[i]
		operation = GetRandomOperation(property, domainObjects)
		if (property != None):
			domainInitialSet.append(operation)
	
	for i in range(0, SafeRandomRange(MinAmountOfAuthorGoals, MaxAmountOfAuthorGoals)):
		if i == 0: domainAuthorGoals += str(GetRandomOperation(domainProperties[0], domainObjects))
		else: domainAuthorGoals += " | " + str(GetRandomOperation(domainProperties[0], domainObjects))
			
	print("domain: \"" + str(uuid.uuid4()) + "\"")
	
	print("goal: (" + domainAuthorGoals + ")")

	for type in domainTypes:
		print(type)
		
	for object in domainObjects:
		print(object)
		
	for property in domainProperties:
		print(property)
		
	for initialState in domainInitialSet:
		print(initialState)
		
	print()

path = 'data/'
with open(path + 'actions.txt', 'r') as file:
	actions = file.read().splitlines();
	
with open(path + 'objects.txt', 'r') as file:
	objects = file.read().splitlines();

with open(path + 'properties.txt', 'r') as file:
	properties = file.read().splitlines();

with open(path + 'types.txt', 'r') as file:
	types = file.read().splitlines();

while True:
    Main()
    if input() == 'q':
        break;