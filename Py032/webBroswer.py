#This tutorial should teach us how to use documentation
#Really? this is not the tutorial I expected...
#But this webbrowser module looks interest, perhaps is not for testing but
#Something can be automatized.
import webbrowser
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
webbrowser.get(chrome_path).open("http://google.com")


# chrome.open("https://www.python.org/")

# help(webbrowser)