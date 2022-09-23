#############################################################################
#																# - # = # X #
#############################################################################
#				Downloads stuff from CWS via Tor Browser					#
#		Tor doesn't load? Make sure to enable bridges in your settings!		#
#																			#
#																			#
# Made for Cyber laptops, because BitWarden doesn't deserve to be blocked	#
#			- Dex															#
#																			#
#		https://github.com/Lamby777/ExtensionRipper							#
#														#####################
#	I drank the Kool-Aid. Oh yeahhhhh!					#	OK	#	Cancel	#
#############################################################################

import os

print("Path to Tor Browser binary (leave blank for C:\\Tor Browser\\firefox.exe)")
tor_path = input()

if tor_path == "":
	tor_path = "C:\\Tor Browser\\firefox.exe"

cmd = "\"" + tor_path + "\" -new-tab \"{url}\""



ext_ids = []

while True:
	print("ID of Chrome Extension? (leave empty to download queue)")
	id = input()

	if id == "":
		break

	ext_ids.append(id)



for ext_id in ext_ids:
	url = "https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D"+ext_id+"%26installsource%3Dondemand%26uc"
	fcmd = cmd.format(url=url)

	print(fcmd)

	os.system(fcmd)
