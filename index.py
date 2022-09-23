print("ID of Chrome Extension:")
ext_id = input()

url = "https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D"+ext_id+"%26installsource%3Dondemand%26uc"

from torpy.http.requests import TorRequests

response = None

with TorRequests() as tor_requests:
	with tor_requests.get_session() as session:
		response = session.get(url)

with open(ext_id+".zip", "wb") as f:
	f.write(response.raw())
