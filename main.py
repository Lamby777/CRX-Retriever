#############################################################################
#																# - # = # X #
#############################################################################
#			  Downloads stuff from CWS via Google CWS Clients2				#
#																			#
# Made for Cyber laptops, because BitWarden doesn't deserve to be blocked	#
#			- Dex															#
#																			#
#		https://github.com/Lamby777/ExtensionRipper							#
#														#####################
#	I drank the Kool-Aid. Oh yeahhhhh!					#	OK	#	Cancel	#
#############################################################################

import requests
from zipfile import ZipFile
from os import path, remove

# If the CWS API ever changes, update this URL.
# The rest of the script is probably gonna work fine.
url = "https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D{0}%26installsource%3Dondemand%26uc"

# Finds URI of user's desktop
homedir = path.expanduser("~")
desktop_path = path.join(homedir, "Desktop")


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
	relpath = path.join(desktop_path, ext_id)

	# Save the file
	with open(relpath+".crx", "wb") as f:
		f.write(res.content)

		with ZipFile(relpath+".crx","r") as zip_ref:
			fext_path = path.join(
				path.expanduser("~"),
				"Documents/Unpacked Extensions",
				ext_id
			)

			zip_ref.extractall(fext_path)
		
	remove(relpath + ".crx")

	print("Saved extension " + ext_id + "...")
		


print("\n\nDone! To finish installations, go to brave://extensions in the browser, and follow these steps:")
print(" - Enable Developer Mode if it's not already enabled")
print(" - Click \"Load Unpacked Extension\" and select the folder of the extension you want to install.")
print(" - Repeat the last step for each extension you want to install.")
print("\nThis app saves folders to a folder called \"Unpacked Extensions\" in your LOCAL Documents folder.\n")
print("##############################################################################################################")
print("#                                                                                                            #")
print("#     IMPORTANT - IF YOU CAN'T FIND IT, YOU'RE PROBABLY LOOKING IN YOUR ONEDRIVE DOCUMENTS FOLDER!!!!!!!     #")
print("#                                                                                                            #")
print("##############################################################################################################\n\n\n")

print("Press Enter to exit.\n")
input()
