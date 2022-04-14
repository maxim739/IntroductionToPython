import json

filename3 = 'json_files/username2.json'

try:
	with open(filename3) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename3, 'w') as f:
		json.dump(username, f)
		print(f"We will remember you when you come back {username}. ")