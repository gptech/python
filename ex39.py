#creates a mapping of states to abbreviation

#This is an example of a dictionary
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

#creates a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#Print out some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#Print every state abbreviation. The for loop creates the variable within the scope of the loop. so the first item is the key and the
#second item is the abbreviation or 'value' as the dictionary sees it. 
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s " % (state, abbrev)

#Now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

#Now safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city