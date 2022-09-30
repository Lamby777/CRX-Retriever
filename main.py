#############################################################################
#																# - # = # X #
#############################################################################
#			  Downloads stuff from CWS via Google CWS Clients2				#
#																			#
# Made for Cyber laptops, because BitWarden doesn't deserve to be blocked	#
#			- Dex															#
#																			#
#		https://github.com/Lamby777/CRX-Retriever							#
#														#####################
#	I drank the Kool-Aid. Oh yeahhhhh!					#	OK	#	Cancel	#
#############################################################################

import requests
from zipfile import ZipFile
from os import path, remove, mkdir

# If the CWS API ever changes, update this URL.
# The rest of the script is probably gonna work fine.
url = "https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D{0}%26installsource%3Dondemand%26uc"

# Finds URI of user's desktop
output_path = path.normpath("C:\\Unpacked Extensions")

try:
	mkdir(output_path)
except FileExistsError:
    pass

ext_ids = []

while True:
	print("ID of Chrome Extension? (leave empty to download queue)")
	id = input()

	# If input empty, start downloading
	if id == "":
		break

	# Otherwise, add the input onto the list
	ext_ids.append(id)

print("Loading...")

for ext_id in ext_ids:
	# GET request the crx file
	res = requests.get(url.format(ext_id))
	relpath = path.join(output_path, ext_id)

	# Save the file
	with open(relpath+".crx", "wb") as f:
		f.write(res.content)

		with ZipFile(relpath+".crx","r") as zip_ref:
			zip_ref.extractall(relpath)
		
	remove(relpath + ".crx")

	print("Saved extension " + ext_id + "...")
		


print("\n\nDone! To finish installations, go to brave://extensions in the browser, and follow these steps:")
print(" - Enable Developer Mode if it's not already enabled")
print(" - Click \"Load Unpacked Extension\" and select the folder of the extension you want to install.")
print(" - Repeat the last step for each extension you want to install.")
print("\nThis program saves folders to C:\\Unpacked Extensions.\n\n\n")

print("Press Enter to exit.\n")
input()
