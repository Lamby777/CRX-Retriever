# Introduction

Welcome to the manual for `CRX-R`, a script I wrote for this class to be able to download themes and extensions over the Chrome Web Store on the school filter without getting the `CRX_HEADER_INVALID` error. 

# Manual

First, go to the [releases page](https://github.com/Lamby777/CRX-Retriever/releases) and download the latest build (or if you already downloaded Python onto the school computer, you can download the source code and run `main.py` from the terminal).

![GitHub Releases page](/readmeData/download.png)

Extract the folder, and open it up.

![Extracted folder](/readmeData/extract.png)

Now, go over to the Chrome Web Store and find the extension(s) you want to download. Don't actually download it, but just check its page. The URL will contain an extension ID like this (highlighted):

![Get ID of extension](/readmeData/get-id.png)

Copy this ID, and paste it into the app. If CTRL+V isn't working, try right clicking. Make sure the title bar of the app doesn't say "Select." If it does, that means you have selected some text, and you need to unselect it before pasting (press <kbd>Backspace</kbd>, <kbd>Esc</kbd>, or similar keys to deselect).

![Paste IDs into app](/readmeData/pasting.png)

After you've queued all your needed extensions into the app, press enter on an empty line to submit. The app will download them onto your desktop one-by-one, unpack them into the folder
`C:\Users\{you}\Documents\Unpacked Extensions`, and finally, it will
delete the downloaded CRX from your desktop.

Follow the instructions it gives in the terminal, or if you want, keep reading this manual. They both contain the same instructions.

![Submit IDs](/readmeData/run-script.png)

After you ran the script, open Brave Browser, and go to Settings >> Extensions.

![Open Extensions Settings](/readmeData/open-settings.png)

Enable Developer Mode on the top right, if it isn't already. For each extension you want to install, click "Load Unpacked Extensions" and navigate to its folder in
`C:\Users\{you}\Documents\Unpacked Extensions`. Once finished, make sure that you __DON'T DELETE THE FOLDER__! It's not a temporary file, and your extensions ___WILL DISAPPEAR___ if you delete the unpacked folder! If your extensions disappear, it's not a bug with this app, so make sure your `Unpacked Extensions` folder is still full!

![Load Unpacked Extension](/readmeData/load-unpacked.png)

Congratulations, you just got around Lightspeed Systems's CRX-integrity-breaking spyware. Here are some extensions you might want to download:

| Extension/Theme 	| ID 	
|-----------	    |----	
| ClassLink         | `jgfbgkjjlonelmpenhpfeeljjlcgnkpe`    	
| BitWarden         | `nngceckbapebfimnlniiiahkandclblb`
| uBlock Origin     | `cjpalhdlnbpafiamejdnhcphjbkeiagm`
| Carbon Theme      | `eokjilkfeplbkpbefpnhkcfaaflellba`

<br>

---

<br>

[Chrome Web Store (find your own extension IDs here)](https://chrome.google.com/webstore/category/extensions?hl=en)

<br>

---

<br>

___GG EZ___

\- Dex <3
