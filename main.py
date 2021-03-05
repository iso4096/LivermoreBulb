import subprocess
import time

from datetime import datetime
from threading import Thread
from flask import Flask
app = Flask(__name__)

app_content = open("index.html", "r").read()

# http://centennialbulb.org/oldbulb/ctbulb.jpg


@app.route('/')
def main():
	global times, app_content
	return app_content % (times)


def run():
	app.run(host="0.0.0.0", port=8000)


def keep_alive():
	server.start()


keep_alive()

times = 0
attempts = 0
prev_response = None
while True:
	now = datetime.now()

	if now.microsecond <= 50:
		response = subprocess.run([
		    'curl', 'http://centennialbulb.org/oldbulb/ctbulb.jpg', '-s',
		    '--output', '-'
		],
		                          stdout=subprocess.PIPE).stdout
		if prev_response != response and len(response) > 30000:
			file_name = time.strftime("images/%Y%m%dT%H%M%SZ.jpg",
			                          time.localtime())
			with open(file_name, 'wb') as image_file:
				image_file.write(response)
			prev_response = response
			times += 1
			attempts = 0
		else:
			attempts += 1

		print(times, attempts)
