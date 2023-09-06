# ifdl
A Python script to retrieve all image links from an ImageFap gallery. The links will be copied to the clipboard, after which any mass file downloader can be used. 

## Requirements for the script
Install the required libaries using: ```pip install urllib3 numpy pyperclip```. This is not needed to run the executable ([ifdl.exe](ifdl.exe)).

## Using the script
The script [ifdl.py](ifdl.py) or the executable [ifdl.exe](ifdl.exe) can be run. 

## Notes
- When using the script ([ifdl.py](ifdl.py)), the bot detection prevention can be tweeked. The average time between requests is 2 seconds, because bot detection caught on when 1 second was used.
- When a 302 error occurs, open a new browser window and visit the gallery page to complete a reCAPTCHA. 
- The executable keeps getting flagged as virus, so I took it down for the moment.
