from torpy import TorClient

print("ID of Chrome Extension:")
ext_id = input()

url = "https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3Dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx%26installsource%3Dondemand%26uc"

from torpy.http.requests import TorRequests
with TorRequests() as tor_requests:
	with tor_requests.get_session() as session:
		response = session.get(url)

with open("filename.txt", "wb") as f:
	response.raw()
