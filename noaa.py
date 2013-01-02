def get_token(token_file = 'noaa.token'):
	try:
		f = open(token_file, 'r')
		data = f.read()
		f.close()
	except Excetion, e:
		data = ''

	return data

class Station(object):
	def __init__(self):
		self.id = ''
		self.name = ''
		self.latitude = 0
		self.longitude = 0
		self.min_date = ''
		self.max_date = ''
		self.usable = False

	def __init__(self, sid, name, min_date, max_date, usable):
		self.id = sid
		self.name = name
		self.min_date = min_date
		self.max_date = max_date
		self.usable = usable
		self.latitude = 0
		self.longitude = 0

	def __init__(self, sid, name, latitude, longitude):
		self.id = sid
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.min_date = ''
		self.max_date = ''
		self.usable = False

	def __str__(self):
		return ('(%s) %s [%s,%s] min: %s, max: %s (usable: %s)'
				% (self.id, self.name, self.latitude, self.longitude, 
				self.min_date, self.max_date, self.usable))