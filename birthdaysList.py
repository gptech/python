
#dictionary
birthdays = {"Luke Skywalker": "5/24/19", "Obi-Wan Kenobi": "3/11/57", "Darth Vadar": "4/1/41"}

if "Yoda" in birthdays:

	print ""

else:

	birthdays["Yoda"] = "Unknown"

if "Darth Vadar" in birthdays:

	print ""

else:

	birthdays["Darth Vadar"] = "Unknown"

#not sure why this works but this will give you the value of each key
for birthday in birthdays:
	print birthday, birthdays[birthday]

del(birthdays["Darth Vadar"])

print birthdays

birthdays = dict(LukeSkywalker= "5/24/19", ObiWanKenobi="3/11/57", DarthVadar="4/1/41")

print birthdays


