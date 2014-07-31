

import sqlite3

class LogMessage:

	#creates an instance of a database when you call this class with dbname
	def __init__(self, dbname):

		self.dbname = dbname

		db = sqlite3.connect(self.dbname)

		db.execute('create table if not exists LogMessage (message)')

		db.commit()

		db.close()

	# will open up the database and read the messages
	def read(self):

		db = sqlite3.connect(self.dbname)

		data = db.execute ('Select * from LogMessage')

		for each in data:
			print(each)

		db.close()

	#Will write something to the LogMessage variables
	def write(self, message):

		db = sqlite3.connect(self.dbname)

		db.execute('insert into LogMessage (message) values (?)', (message,))

		db.commit()

		db.close()

#This just runs through everything because it wouldn't import for some reason.
log =LogMessage('test.db')
log.write('Testing')
log.write("Test")
log.read()