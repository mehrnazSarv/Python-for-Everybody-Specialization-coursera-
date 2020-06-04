
import urllib.request,  urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter location: ")
address = urllib.request.urlopen(url , context = ctx).read()


total = 0
while True:
	if len(url)<1: break

	print("Retrieving: ", address)
	print("Retrieved ", len(address)," characters")

	info = json.loads(address)
	info = info["comments"]
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
		print("Sum: ", total)
	print("Final sum: ", total)
	break
