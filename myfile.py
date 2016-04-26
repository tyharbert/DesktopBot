import simplejson as json

def save(file_path, data):
	f = open(file_path, "w")
	json_data = json.dumps(data)

	f.write(json_data)
	f.close()

def load(file_path):
	f = open(file_path, "r")
	enc = f.read()
	
	f.close()
	return json.loads(enc)
